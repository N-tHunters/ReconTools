#!/usr/bin/env python3
import requests
import sys
from urllib3.exceptions import InsecureRequestWarning


requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)


base_urls = []
with open(sys.argv[1]) as f:
    base_urls = [i.strip() for i in f.readlines() if i.strip() != '']

for url in base_urls:
    cms = ""
    try:
        wp_login = url + "/wp-login.php"
        response = requests.get(wp_login, allow_redirects=False, verify=False)
        if response.status_code == 200:
            cms = "Wordpress"

        joomla_login = url + "/administrator/"
        response = requests.get(joomla_login, allow_redirects=False, verify=False)
        if response.status_code == 200 and 'Joomla!' in response.text:
            cms = "Joomla"

        moodle_logo = url
        response = requests.get(url, allow_redirects=False, verify=False)
        if response.status_code == 200 and 'src="pix/moodlelogo.gif"' in response.text:
            cms = "Moodle"
    except requests.exceptions.SSLError:
        pass
    print(f'"{url}","{cms}"')
