#!/usr/bin/env python3
import requests
import csv
import sys
import subprocess

wp_urls = []
with open(sys.argv[1]) as f:
    reader = csv.reader(f)
    for row in reader:
        url, cms = row
        if cms.strip() == 'Wordpress':
            wp_urls.append(url)


for url in wp_urls:
    p = subprocess.Popen(["./enumerate_wordpress_users.sh", url, sys.argv[2], url.split('/')[1]], stdout=subprocess.PIPE)
    out, err = p.communicate()
    out = out.decode()
    users = out.split('\n')
    for user in users:
        if user.strip() == '': continue
        print(f'"{user}","{url}"')
