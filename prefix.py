# prefix challenge

import requests

token = '2fcee296e6c330db9546388265dcc3af'

auth = {
    'token':token
}
# connect to api
prefix_req = requests.post('http://challenge.code2040.org/api/prefix', json=auth)

# pull out our prefix that the string starts with
prefix = prefix_req.json()['prefix']

# pull out our array of strings that we have
array_of_strings = prefix_req.json()['array']

# our array that will contains strings that do not include the prefix
strings_do_not_contain_prefix = list()

# loop over our strings of arrays
for string in array_of_strings:
    # if our string does not with the prefix, we add it to our array of strings
    if not string.startswith(prefix):
        strings_do_not_contain_prefix.append(string)

# add our prefix string array to our solution dictionary and send it to the server
solution = {
    'token':token,
    'array':strings_do_not_contain_prefix
}
solution_req = requests.post('http://challenge.code2040.org/api/prefix/validate', json=solution)
print('response: {}'.format(solution_req.text))  # response from server
