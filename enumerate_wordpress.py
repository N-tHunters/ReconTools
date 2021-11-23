#!/usr/bin/env python3
import requests
import csv
import sys
import subprocess


def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)
    sys.stderr.flush()


wp_urls = []
with open(sys.argv[1]) as f:
    reader = csv.reader(f)
    for row in reader:
        url, cms = row
        if cms.strip() == 'Wordpress':
            wp_urls.append(url)


for url in wp_urls:
    eprint(f"[o] Enumerating {url} wordpress")
    eprint(" Enumerating users...", end='')
    p = subprocess.Popen(["./enumerate_wordpress_users.sh", url, sys.argv[2], url.split('//')[1].split('/')[0]], stdout=subprocess.PIPE)
    out, err = p.communicate()
    out = out.decode()
    users = out.split('\n')
    for user in users:
        if user.strip() == '': continue
        print(f'"{user}","{url}"')
    eprint('done')
    eprint(" Bruteforcing passwords...", end='')
    eprint("done")
