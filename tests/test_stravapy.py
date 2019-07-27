from stravapy.oauth.utils import OAuth2Client


with open('APIVARS.txt', 'r') as file:
    var = file.read()
    strava = {'id': var.split(':')[1][:5],
              'secret': var.split(':')[2]}

auth_params = {'response_type': 'code',
               'approval_prompt': 'force',
               'scope': 'read,activity:read_all'}

strava_client = OAuth2Client(client_id=strava['id'],
                             client_secret=strava['secret'],
                             redirect_uri='http://localhost:8080/',
                             access_token_url='https://www.strava.com/oauth/token',
                             base_url='https://www.strava.com',
                             authorize_url='https://www.strava.com/oauth/authorize',
                             auth_params=auth_params)

strava_client.authenticate_user()


