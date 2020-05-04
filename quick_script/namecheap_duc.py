#!/usr/bin/python3

# Dynamic Update client for Namecheap DDNS
# This is quicker standalone from the module
import requests as r

HOST = None
DOMAIN = 'example.com'
PASSWORD = 'asd;flj4879puoiq2l3jlk;asdf'
SITE_URL = 'https://dynamicdns.park-your-domain.com'
PATH = '/update'

params = {'host': HOST, 'domain': DOMAIN, 'password': PASSWORD}

session = r.get(SITE_URL + PATH, params=params)
print(session.url)
print(session.status_code)
print(session.text)
