# needle in haystack challenge

import requests

token = '2fcee296e6c330db9546388265dcc3af'

auth = {
    'token':token
}

needle_req = requests.post('http://challenge.code2040.org/api/haystack', json=auth)

# pull out our haystack and our needle from the json we get back
haystack = needle_req.json()['haystack']
needle = needle_req.json()['needle']

# counter to keep track of our index
counter = 0

# loop over our haystack
for hay in haystack:
    if hay == needle:
        print('counter is: {}'.format(counter))  # print out the index where our needle is
        break  # break out of our loop
    counter += 1  # increment counter. python doesn't support ++ operator

solution = {
    'token':token,
    'needle':counter
}

# send the index of the needle back to the api
solution_req = requests.post('http://challenge.code2040.org/api/haystack/validate', json=solution)
print('response: {}'.format(solution_req.text))  # print out whether we are complete or not
