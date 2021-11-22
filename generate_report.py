#!/usr/bin/env python3
import jinja2
import sys
import os
import csv


base_dir = sys.argv[1]
server_version_file = os.path.join(base_dir, 'serverversions.csv')
cms_file = os.path.join(base_dir, 'cms.csv')

sites = dict()
with open(server_version_file) as f:
    reader = csv.reader(f)
    for row in reader:
        url, server = row
        if sites.get(url) is None:
            sites[url] = dict()
        sites[url]['server'] = server


with open(cms_file) as f:
    reader = csv.reader(f)
    for row in reader:
        url, cms = row
        if sites.get(url) is None:
            sites[url] = dict()
        sites[url]['cms'] = cms


sites_list = []
for url in sites:
    sites_list.append({'url': url, 'server': sites[url]['server'], 'cms': sites[url]['cms']})


template_loader = jinja2.FileSystemLoader("./templates")
template_env = jinja2.Environment(loader=template_loader)
template = template_env.get_template('report.html')

output = template.render(
                      target=sys.argv[2],
                      sites=sites_list
)

print(output)
