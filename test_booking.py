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
    ##GIVEN - webservice url in order to GET Booking IDs
    url="https://restful-booker.herokuapp.com/booking"
    resp = requests.get(url)
    json_resp = resp.json()
    """ ##VERY LONG TEST CHECKING EACH ID
    ##WHEN - using any of existing IDs
    for i in range(0, len(json_resp)):
        ##GIVEN - existing booking ID at the end of webservice url
        id=json_resp[i]['bookingid']
        urlid=url+"/"+str(id)
        ##WHEN - GET Booking
        respo = requests.get(urlid)
        json_respo = respo.json()
        ##THEN - Response has correct code
        assert respo.status_code==200, "Wrong response code."
        ##THEN - Response all booking details in correct format
    """
    ##GIVEN - webservice url and random ID
    pos=random.randrange(0,len(json_resp))
    id=json_resp[pos]['bookingid']
    urlid=url+"/"+str(id)
    ##WHEN - GET Booking using existing ID
    respo = requests.get(urlid)
    json_respo = respo.json()
    ##THEN - Response has correct code
    assert respo.status_code==200, "Wrong response code."
    ##THEN - Response all booking details with expected names
    assert list(json_respo.keys())[0]=="firstname", "Data key 'firstname' does not exists"
    assert list(json_respo.keys())[1]=="lastname", "Data key 'lastname' does not exists"
    assert list(json_respo.keys())[2]=="totalprice", "Data key 'totalprice' does not exists"
    assert list(json_respo.keys())[3]=="depositpaid", "Data key 'depositpaid' does not exists"
    assert list(json_respo.keys())[4]=="bookingdates", "Data key 'bookingdates' does not exists"
    assert list(json_respo['bookingdates'].keys())[0]=="checkin", "Data key 'checkin' does not exists"
    assert list(json_respo['bookingdates'].keys())[1]=="checkout", "Data key 'checkout' does not exists"
    assert list(json_respo.keys())[5]=="additionalneeds", "Data key 'additionalneeds' does not exists"
    ##THEN - Response all booking details with expected types
    assert isinstance((json_respo['firstname']), str) , "'firstname' is not a string - unexpected type"
    assert isinstance((json_respo['lastname']), str) , "'lastname' is not a string - unexpected type"
    assert isinstance((json_respo['totalprice']), (int, float)) , "'totalprice' is not a intiger nor float - unexpected type"
    assert isinstance((json_respo['depositpaid']), bool) , "'depositpaid' is not a bool - unexpected type"
    assert isinstance((json_respo['bookingdates']), dict) , "'bookingdates' is not a dictionary - unexpected type"
    checkin=json_respo['bookingdates']['checkin']
    validate(checkin)
    assert isinstance(datetime.datetime.strptime(checkin, '%Y-%m-%d'), datetime.date) , "'checkin' is not a date- unexpected type"
    checkout=json_respo['bookingdates']['checkout']
    validate(checkout)
    assert isinstance(datetime.datetime.strptime(checkout, '%Y-%m-%d'), datetime.date) , "'checkin' is not a date- unexpected type"
    assert isinstance((json_respo['additionalneeds']), str) , "'additionalneeds' is not a string - unexpected type"
    ##WHEN - GET Booking using unexisting ID
    maxID=find_maxID(json_resp)
    id=maxID+1
    urlid=url+"/"+str(id)
    respo = requests.get(urlid)
    assert respo.status_code==404, "Wrong response for unexisting ID"





