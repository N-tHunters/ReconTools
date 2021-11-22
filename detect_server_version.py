#!/usr/bin/env python3
import requests
import sys
from urllib3.exceptions import InsecureRequestWarning


requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)


urls = []
with open(sys.argv[1]) as f:
    urls = [i.strip() for i in f.readlines() if i.strip() != '']


for url in urls:
    version = ''
    try:
        response = requests.options(url, verify=False)
        version = response.headers.get('Server')
        if version is None:
            version = ''
    except requests.exceptions.SSLError:
        pass
    print(f'"{url}","{version}"')
