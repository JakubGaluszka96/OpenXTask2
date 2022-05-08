from tokenize import Number
import pytest
import requests
import json
import jsonpath

def test_GetBookingIds():
    url="https://restful-booker.herokuapp.com/booking"
    resp = requests.get(url)
    json_resp = resp.json()
    assert resp.status_code==200, "Wrong response code."
    for i in range(0,len(json_resp)):
        assert "bookingid" in json_resp[i] , "Data key has changed"
    for i in range(0,len(json_resp)):
        assert isinstance((json_resp[i]['bookingid']), int) , "At least one of booking Id's is not an intiger"



url="https://restful-booker.herokuapp.com/booking"
resp = requests.get(url)
json_resp = resp.json()
print(json_resp[0])
print("bookingid" in json_resp[0])
#print(resp.headers)
#print(resp.cookies)
#print(resp.encoding)
#print(resp.url)







