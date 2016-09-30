import pytest
import requests

def http_request(url):
  r = requests.get(url)
  return r

def test_good_http_request():
  assert http_request('http://haproxy/web').status_code == 200

def test_bad_http_request():
  assert http_request('http://haproxy/blah').status_code == 503
