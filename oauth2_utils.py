# -*- coding: utf-8 -*-
"""
Created on Mon Jul 22 12:55:38 2019

@author: wrush049
"""
import urllib
import os
import json
import webbrowser
import time
from http.server import HTTPServer, BaseHTTPRequestHandler


class AuthServerRequestHandler(BaseHTTPRequestHandler):
    """
    Listen for one http request on port then close and return request query
    The request handler for the authentication process
    Runs so that the redirect to localhost:<port> is handled
    """

    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        # self.server is the server object instance that is being used
        self.server.token_code = self.parse_code()

        # Generate the screen that the user will see
        html_file = os.path.join(
            os.path.dirname(os.path.realpath(__file__)), "templates", "success.html"
        )
        with open(html_file, "rb") as html_view:
            self.wfile.write(html_view.read())

    def parse_code(self):
        """
        Parse the token code from the redirect URL
        """
        code = self.path.split("=")[2].split("&")[0]
        return code


class OAuth2Client:
    """
    An OAuth2 user object for Strava
    
    **params is used in place of standard **kwargs here to indicate that the 
    keyworded arguments are parameters for the url calls
    """

    def __init__(
        self,
        client_id,
        client_secret,
        redirect_uri,
        auth_params=None,
        access_token_url=None,
        base_url=None,
        authorize_url=None,
        user_auth_url=None,
        state=os.urandom(2),
        access_token=None,
        token_code=None,
        token_dict=None,
    ):
        """
        Instantiate an OAuthClient object with relevant params
        
        :param state: A random int provided to the Strava server that must be 
                        returned. Protects again CSRF attacks. Currently not enabled
        """
        self.client_id = client_id
        self.client_secret = client_secret
        self.access_token_url = access_token_url
        self.base_url = base_url
        self.auth_params = auth_params
        self.redirect_uri = redirect_uri
        self.authorize_url = authorize_url
        self.token_dict = token_dict
        self.access_token = access_token
        self.user_auth_url = user_auth_url

    def authenticate_user(self, host="", port=8080, handler=AuthServerRequestHandler):
        """
        Puts together the class functions to authenticate the user. 
        Steps:
            1. Generate the authorization URL with parameter payload
            2. Create an HTTP server instance to accept provider redirect
            3. Open the authentication webpace using system browser default
            4. Allow local server to handle the redirect request
            5. Pull the token code from the url of the redirect request
            6. Close the local server instance
            7. Exchange the code for an access token
            8. Set the athlete 'access_token' attribute with token id
            
        :param host: The host address for the server. "" == 'localhost' == 127.0.0.1
        :param port: Socket port for server to listen on. Default 8080
        :param handler: The request handler for the server. Default is custom 
                        handler for OAuth2 authentication specifically.
        """
        self.get_authorize_url(**self.auth_params)
        httpd = HTTPServer((host, port), handler)
        webbrowser.open(self.user_auth_url)
        httpd.handle_request()
        self.token_code = httpd.token_code
        httpd.server_close()

        # exchange_code_for_token sets attr 'token_dict'
        self.exchange_code_for_token()
        self.access_token = self.token_dict["access_token"]

    def refresh_token(self, **params):
        """
        Request a refresh token from the token endpoint.
        If the 'expires_in' parameter is more than 3,600s (1 hr) away, just 
        return the current access token. (Strava will do the same)
        
        'expires_in' will be calculated if return dict does not contain it
        """
        if self.token_dict["expires_in"] >= 3600:
            return self.access_token
        elif self.token_dict["expires_in"] < 3600:
            if not params:
                params = dict()
            params.update(
                {
                    "client_id": self.client_id,
                    "client_secret": self.client_secret,
                    "grant_type": "refresh_token",
                    "refresh_token": self.token_dict["refresh_token"],
                }
            )

        payload = urllib.parse.urlencode(params).encode()

        # Send a POST request to the Strava Token endpoint and decode base
        req = urllib.request.Request(self.access_token_url, data=payload)
        resp = urllib.request.urlopen(req).read()
        self.token_dict = json.loads(resp)
        if not self.token_dict["expires_in"]:
            self.token_dict["expires_in"] = self.token_dict["expires_at"] - int(
                time.time()
            )

    def get_authorize_url(self, **params):
        """
        Returns a formatted authorize URL.
        :param **params: Additional keyworded arguments to be added to the
            URL querystring.
        :type **params: dict
        """
        if not params:
            params = dict()

        params.update({"client_id": self.client_id, "redirect_uri": self.redirect_uri})
        self.user_auth_url = self.authorize_url + "?" + urllib.parse.urlencode(params)
        return self.user_auth_url

    # TODO the keyworded params argument is inaccessible from outside the class
    def exchange_code_for_token(self, **params):
        """
        Exchange the code returned to the redirect uri for an access token
        """
        if not params:
            params = dict()
        params.update(
            {
                "client_id": self.client_id,
                "client_secret": self.client_secret,
                "code": self.token_code,
                "grant_type": "authorization_code",
            }
        )

        payload = urllib.parse.urlencode(params).encode()
        # Send a POST request to the Strava Token endpoint and decode base
        req = urllib.request.Request(self.access_token_url, data=payload)
        resp = urllib.request.urlopen(req).read()
        self.token_dict = json.loads(resp)
