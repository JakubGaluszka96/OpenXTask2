import pytest
import requests
import json
import jsonpath

def test_GetBookingIds():
    ##GIVEN - webiservice url in order to GET
    url="https://restful-booker.herokuapp.com/booking"
    ##WHEN - GET booking
    resp = requests.get(url)
    json_resp = resp.json()
    ##THEN - Response all booking IDs in correct format
    assert resp.status_code==200, "Wrong response code."
    for i in range(0,len(json_resp)):
        assert "bookingid" == list(json_resp[i].keys())[0] , "Data key does not exists"
        assert isinstance((json_resp[i]['bookingid']), int) , "At least one of booking Id's is not an intiger"
        


url="https://restful-booker.herokuapp.com/booking"
resp = requests.get(url)
json_resp = resp.json()
keys = list(json_resp[2].keys())[0]
print(type(keys))
#print(resp.headers)
#print(resp.cookies)
#print(resp.encoding)
#print(resp.url)







