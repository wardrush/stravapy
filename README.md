# stravapy
#### Version 0.1
A tool to interact with [Strava API v3](https://developers.strava.com/) without requiring an existing web framework

## Installation
TODO 

## Requirements

## Motivation
The existing [Stravalib library](https://github.com/hozn/stravalib "Stravalib GitHub") is appropriate if there is an existing web framework, but I wanted to create my own version of the [Elevate Strava web extension](https://thomaschampagne.github.io/elevate/#/landing "Elevate Strava Homepage") in a local environment for personal training analysis. 

## Getting Started
The Strava authentication process generally works as follows:
1. Register with Strava for API access at https://www.strava.com/settings/api
2. Record your Client ID and Client Secret. Make sure that if you're uploading to github, you do not leave these in plaintext
4. TODO figure out exactly what this workflow is going to look like

## Project Structure
Strava is using effectively abstract base classes in the form of meta classes. Meta athletes and activities will be replaced with simply their ids
