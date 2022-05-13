import requests

def Auth():
    url="https://restful-booker.herokuapp.com/auth"
    data={
    "username" : "admin",
    "password" : "password123"
    }
    head='Content-Type: application/json'
    resp=requests.post(url, data, head)
    cookie=resp.json()
    return cookie

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
    ##authorization token in order to delete
    cookie = Auth()
    ##WHEN - GET Booking using existing ID    
    resp = requests.get(url)
    ##THEN - Response must have correct code
    assert resp.status_code==200, "Wrong response code."
    ##THEN - Input data when created must be equal to response data
    assert resp.json()==data
    ##GIVEN - webservice url leading to unexisting booking (just deleted)
    resp = requests.delete(url, cookies=cookie, headers=head)
    assert resp.status_code == 201, "Created sample booking was not deleted"
    ##WHEN - GET Booking using unexisting ID
    resp = requests.get(url)
    ##THEN - Response code should be 404 Not found
    assert resp.status_code==404, "Wrong response for unexisting ID"

def test_Delete_ok():

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
    url=url+"/"+str(id)
    resp = requests.get(url)
    assert resp.status_code == 200, "Booking was not successufly created (for delete purpose)."
    resp = requests.delete(url, cookies=cookie, headers=head)
    assert resp.status_code == 201, "Incorrect response code"
    resp = requests.get(url)
    assert resp.status_code == 404, "Booking was not successfuly deleted"

def test_Delete_no_auth():

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
    resp = requests.get(url)
    assert resp.status_code == 200, "Booking was not successufly created (for delete purpose)."
    resp = requests.delete(url, headers=head)
    assert resp.status_code == 403, "Incorrect response code"
    resp = requests.get(url)
    assert resp.status_code == 200, "Booking was deteted without authorization"

