# dating game challenge
import requests
import datetime

token = '2fcee296e6c330db9546388265dcc3af'

auth = {
    'token':token
}

# make our request to the api
dating_req = requests.post('http://challenge.code2040.org/api/dating', json=auth)

# pull out the datestamp and interval from our json
datestamp = dating_req.json()['datestamp']
interval = dating_req.json()['interval']

# convert our datestamp string to a date object
date_stamp_object = datetime.datetime.strptime(datestamp, '%Y-%m-%dT%H:%M:%SZ')
# add the seconds given by the api to the current time
final_date = date_stamp_object + datetime.timedelta(seconds=interval)
# convert our final date object to a date string
final_date_string = final_date.strftime('%Y-%m-%dT%H:%M:%SZ')

solution = {
    'token':token,
    'datestamp':final_date_string
}

dating_solution_req = requests.post('http://challenge.code2040.org/api/dating/validate', json=solution)
# see if we got it right or not
print(dating_solution_req.text)
