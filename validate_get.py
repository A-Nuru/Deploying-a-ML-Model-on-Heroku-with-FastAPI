"""
Local Api test script
"""
import requests

r = requests.get('http://127.0.0.1:8000')

assert r.status_code == 200

print("Response code: %s" % r.status_code)
print("Response body: %s" % r.json())
