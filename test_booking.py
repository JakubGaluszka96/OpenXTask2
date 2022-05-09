import requests
import random
import datetime

def validate(date_text):
    try:
        datetime.datetime.strptime(date_text, '%Y-%m-%d')
    except ValueError:
        raise ValueError("Incorrect data format, should be YYYY-MM-DD")

def find_maxID(dict):
    max=dict[0]['bookingid']
    for i in range(1,len(dict)):
        newmax=dict[i]['bookingid']
        if newmax>max:
            max=newmax
    return max

def test_Auth_correct_cred():
    ##GIVEN - webservice url, data with correct creditials, correct header
    url="https://restful-booker.herokuapp.com/auth"
    data={
    "username" : "admin",
    "password" : "password123"
    }
    head='Content-Type: application/json'
    ##WHEN - correct request is posted
    resp=requests.post(url, data, head)
    ##THEN - response code must be correct
    assert resp.status_code==200, "Incorrect response code."
    ##THEN Response must contain data in correct format
    assert list(resp.json().keys())[0]=="token", "response data has no key 'token'"
    assert isinstance(resp.json()["token"], str), "token data do not contain string"

def test_Auth_incorrect_cred():
    ##GIVEN - webservice url, data with incorrect creditials, correct header
    url="https://restful-booker.herokuapp.com/auth"
    data={
    "username" : "baduser",
    "password" : "badpass"
    }
    head='Content-Type: application/json'
    ##WHEN - correct request is posted
    resp=requests.post(url, data, head)
    ##THEN - response code must be correct 401 for not authorized - THIS TEST FAILS
    assert resp.status_code==401, "Incorrect response code. This one should be corrected 401 for bad authorization"
    ##THEN - respone must contain reason why access is denied in correct format
    assert list(resp.json().keys())[0]=="reason", "Data key does not exists"
    assert isinstance(resp.json()["reason"], str), "Reason is not a string"

def test_GetBookingIds():
    ##GIVEN - webservice url in order to GET
    url="https://restful-booker.herokuapp.com/booking"
    ##WHEN - GET Booking IDs
    resp = requests.get(url)
    json_resp = resp.json()
    ##THEN - Response all booking IDs in correct format
    assert resp.status_code==200, "Wrong response code."
    for i in range(0,len(json_resp)):
        assert "bookingid" == list(json_resp[i].keys())[0] , "Data key does not exists"
        assert isinstance((json_resp[i]['bookingid']), int) , "At least one of booking Id's is not an intiger"

def test_GetBooking():
    ##GIVEN - webservice url in order to POST - Create new booking and obtain its ID
    url='https://restful-booker.herokuapp.com/booking'
    head = {
    'Content-Type': 'application/json',
    'Accept': 'application/json',
    }
    data = {
        'firstname': 'James',
        'lastname': 'Brown',
        'totalprice': 111,
        'depositpaid': True,
        'bookingdates': {
            'checkin': '2018-01-01',
            'checkout': '2019-01-01',
        },
        'additionalneeds': 'Breakfast',
    }
    resp = requests.post(url, headers=head, json=data)
    id=resp.json()['bookingid']
    url=url+"/"+str(id)
    ##WHEN - GET Booking using existing ID    
    resp = requests.get(url)
    ##THEN - Response must have correct code
    assert resp.status_code==200, "Wrong response code."
    ##THEN - Input data when created must be equal to response data
    assert resp.json()==data
    ##GIVEN - webservice url leading to unexisting booking
    url='https://restful-booker.herokuapp.com/booking'
    resp = requests.get(url)
    maxID=find_maxID(resp.json())
    id=maxID+1
    ##WHEN - GET Booking using unexisting ID
    url=url+"/"+str(id)
    resp = requests.get(url)
    ##THEN - Response code should be 404 Not found
    assert resp.status_code==404, "Wrong response for unexisting ID"

url="https://restful-booker.herokuapp.com/auth"
data={
"username" : "admin",
"password" : "password123"
}
head='Content-Type: application/json'
resp=requests.post(url, data, head)
cookie=resp.json()

url='https://restful-booker.herokuapp.com/booking'
head = {
    'Content-Type': 'application/json',
    'Accept': 'application/json',
}
data = {
    'firstname': 'James',
    'lastname': 'Brown',
    'totalprice': 111,
    'depositpaid': True,
    'bookingdates': {
        'checkin': '2018-01-01',
        'checkout': '2019-01-01',
    },
    'additionalneeds': 'Breakfast',
}
resp = requests.post(url, headers=head, json=data)
id=resp.json()['bookingid']
newbook=resp.json()
print(newbook)
url=url+"/"+str(id)
resp = requests.delete(url, cookies=cookie, headers=head)
print(resp)

