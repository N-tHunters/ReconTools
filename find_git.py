#!/usr/bin/env python3

import requests
import sys

if len(sys.argv) != 2:
	print(f'Usage: {sys.argv[0]} <url>')
	exit(-1)

url = sys.argv[1]

if url[-1] != '/':
	url += '/'

if not url.startswith('http'):
	print(f'Wrong url, perhaps you meant "http://{url}"?')
	exit(-1)

git_dirs = [
	'.git/HEAD',
	'.git/config'
]

fail_codes = (403, 404)

for i in git_dirs:
	test = requests.get(url + i)
	if test.status_code not in fail_codes:
		print('found')
		break
else:
	print('not found')