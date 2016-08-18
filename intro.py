# connect to code2040 api

# use requests python library to make api call
import requests

auth = {
    'token':'2fcee296e6c330db9546388265dcc3af',
    'github':'https://github.com/fadelakin/code2040-2017-application'
}

resp = requests.post('http://challenge.code2040.org/api/register', json=auth)

print('Connected with API: {}'.format(resp.text))
