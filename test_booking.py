import pytest
import requests
import json
import jsonpath
import random

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
    ##WHEN - GET Booking
    respo = requests.get(urlid)
    json_respo = respo.json()
    ##THEN - Response has correct code
    assert respo.status_code==200, "Wrong response code."






url="https://restful-booker.herokuapp.com/booking"
resp = requests.get(url)
json_resp = resp.json()
id=json_resp[0]['bookingid']
print(len(json_resp))
urlid=url+'/'+str(id)
pos=random.randrange(0,len(json_resp))
print(pos)
id=json_resp[pos]['bookingid']
print(id)










