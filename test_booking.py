import pytest
import requests
import json
import jsonpath

def test_GetBookingIds(url="https://restful-booker.herokuapp.com/booking"):
    #url="https://restful-booker.herokuapp.com/booking"
    resp = requests.get(url)
    json_resp = json.loads(resp.text)
    bookingid = jsonpath.jsonpath(json_resp,'bookingid')
    assert resp.status_code==200


url="https://restful-booker.herokuapp.com/booking"
resp = requests.get(url)
json_resp = resp.json()
bookingid = jsonpath.jsonpath(json_resp,'bookingid')
print(json_resp)






