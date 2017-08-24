[![Build Status](https://travis-ci.org/katechorna/test_github_api.svg?branch=master)](https://travis-ci.org/katechorna/test_github_api)

# GitHub API testing
Project is aimed to test GitHub functionality. Tests are organized in BDD format.

## Getting Started
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.
See deployment for notes on how to deploy the project on a live system.

### Installing
Clone the repository:
```
git clone git@github.com:katechorna/test_github_api.git
```

Setup virtual environment and activate it:
```
virtualenv venv --python=python3.6
source venv/bin/activate
```

Install all the required dependencies:
```
pip install -r requirements.txt
```

## Running the tests

To run the tests locally, simply enter the following command into command line:
```
behave
```
**NOTE:** OAuth Non-Web application flow with creating temporary token is used when running tests locally.
Temporary token is deleted after test run.

## Deployment
Travis CI is used. Tests are automatically launched after each branch update.
See the results here:
```
https://travis-ci.org/katechorna/test_github_api
```
**NOTE:** Predefined token is used when running tests on Travis.