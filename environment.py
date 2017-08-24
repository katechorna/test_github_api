import requests
from getpass import getpass

from config import GITHUB_URL

AUTHORIZATION_URL = GITHUB_URL + 'authorizations'


def before_all(context):
    token_parameters = {
        'scopes': ['gist'],
        'note': 'Temporary token for GitHub API testing'
    }
    username = input('Enter your GitHub username: ')
    password = getpass('Enter your GitHub password:')
    context.auth = (username, password)
    response = requests.post(AUTHORIZATION_URL, json=token_parameters, auth=context.auth)
    token_data = response.json()
    context.token_id = token_data['id']
    token = token_data['token']
    context.headers = {'Authorization': 'token {}'.format(token)}


def after_all(context):
    requests.delete('{}/{}'.format(AUTHORIZATION_URL, context.token_id), auth=context.auth)
