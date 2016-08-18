# reverse a string

# use requests python library to make api call
import requests

token = '2fcee296e6c330db9546388265dcc3af'

auth = {
    'token':token
}

# make the post request to get our string
req = requests.post('http://challenge.code2040.org/api/reverse', json=auth)
string = req.text  # get the string we want to reverse

# reverse the string using the negative values slice method in python
# - creates a copy of the string but in reverse order
reversed_string = string[::-1]

print('original string: {}'.format(string))
print('reversed string: {}'.format(reversed_string))

solution = {
    'token':token,
    'string':reversed_string
}

# make the post request to post request to send our solution
solution_req = requests.post('http://challenge.code2040.org/api/reverse/validate', json=solution)

print('response: {}'.format(solution_req.text))
