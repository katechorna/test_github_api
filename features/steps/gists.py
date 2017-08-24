import requests
from behave import given, then

from features.config import GITHUB_URL

GISTS_URL = GITHUB_URL + 'gists'


@given('we verified number of existing gists')
def get_gists_list(context):
    response = requests.get(GISTS_URL, headers=context.headers)
    context.number_of_gists = len(response.json())


@then('we create new gist')
def create_gist(context):
    gist_parameters = {
        'description': 'Test description of newly created gist',
        'files': {
            'gist_test.txt': {'content': 'Test content of newly created gist'}
        }
    }
    response = requests.post(GISTS_URL, headers=context.headers, json=gist_parameters)
    gist_data = response.json()
    context.gist_id = gist_data['id']


@then('we check if number of gists is increased by one')
def compare_lists(context):
    response = requests.get(GISTS_URL, headers=context.headers)
    updated_number_of_gists = len(response.json())
    assert updated_number_of_gists == context.number_of_gists + 1


@then('we delete newly created gist')
def delete_gist(context):
    response = requests.delete('{}/{}'.format(GISTS_URL, context.gist_id), headers=context.headers)
    response.raise_for_status()
