import pytest
import requests
import json
import jsonpath

def test_GetBookingIds(url="https://restful-booker.herokuapp.com/booking"):
    #url="https://restful-booker.herokuapp.com/booking"
    answer = requests.get(url)
    json_answer = json.loads(answer.text)
    bookingid = jsonpath.jsonpath(json_answer,'bookingid')
    assert 200<=answer.status_code<300


url="https://restful-booker.herokuapp.com/booking"
answer = requests.get(url)
json_answer = answer.json()
bookingid = jsonpath.jsonpath(json_answer,'bookingid')
#print(answer.text)
#print(answer.content)
print(bookingid)






