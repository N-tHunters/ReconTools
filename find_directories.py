#!/usr/bin/env python3

from os import system
import os
import sys

if not os.path.isdir('tmp'):
	os.mkdir('tmp')

wordlist_location = sys.args[2] # '/usr/share/seclists/Discovery/Web-Content/common.txt'
url = sys.args[1]
filename = 'gobuster_output'

system(f'gobuster dir -w {wordlist_location} -u {url} -o tmp/{filename} > /dev/null 2> /dev/null')

with open(f'tmp/{filename}') as file:
	urls = file.read()

urls = urls.split('\n')

for i in range(len(urls)):
	if urls[i] == '':
		continue
	urls[i] = urls[i].replace(': ', ':').replace('> ', '>')
	while '  ' in urls[i]:
		urls[i] = urls[i].replace('  ', ' ')
	urls[i] = urls[i].split()

	directory = urls[i][0]
	status = urls[i][1].replace('(Status:', '').replace(')', '')

	current_url = {'url':directory, 'status':status}

	if status == '301':
		redirect_url = urls[i][3].replace('[-->', '').replace(']', '')
		current_url['redirect url'] = redirect_url

	print(','.join(list(map(lambda x:f'"{current_url[x]}"', current_url))))

os.system(f'rm tmp/{filename}')