#!/usr/bin/env python3
import requests
import sys
from urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)


urls = []
with open(sys.argv[1]) as f:
    urls = [i.strip() for i in f.readlines() if i.strip() != '']


for url in urls:
    redirect = ''
    response = requests.get(url, follow_redirects=False, verify=False)
    if response.status_code == 301:
        redirect = response.headers.get('Location', '')
    print(f'"{url}","{redirect}"')
