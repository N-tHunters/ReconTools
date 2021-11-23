#!/usr/bin/env python3
import requests
import sys
from urllib3.exceptions import InsecureRequestWarning


requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)

for line in sys.stdin:
    url = line.strip()
    if url == '': continue
    response = requests.get(url, verify=False, allow_redirects=False)
    if response.status_code == 200:
        print(url)
