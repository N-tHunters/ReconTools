#!/bin/bash

target_domain=$1
base_dir=targets/$1

echo "Performing initial reconnaissance on $1"
echo "Results will be stored in $base_dir"

mkdir -p $base_dir

echo "[o] Starting subdomains scan..."
sublist3r -d $1 -o $base_dir/subdomains.txt >/dev/null
echo "[+] Subdomains scan finished"

echo "[o] Finding subdomains with HTTP and HTTPS"
cat $base_dir/subdomains.txt | httprobe-bin | sort -u > $base_dir/httpsites.txt
echo "[+] Subdomains with HTTP and HTTPS collected"

echo "[o] Identifying common CMS"
./detect_common_cms.py $base_dir/httpsites.txt > $base_dir/cms.csv
echo "[+] CMS identification finished"

echo "[o] Detecting web-server versions"
./detect_server_version.py $base_dir/httpsites.txt > $base_dir/serverversions.csv
echo "[+] Version identification finished"

echo "[o] Generating HTML report"
./generate_report.py $base_dir/ $target_domain > $base_dir/report.html
echo "[+] Finished"
