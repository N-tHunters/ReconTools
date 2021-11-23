# Auto information collection toolchain
This toolchain is dedicated to collect information about target domain and subdomains

## Scripts:
```bash
./initial_recon.sh <domain>
```

```bash
cat httpsites.txt | ./clear_http.py
```

```bash
cat httpsites.txt | ./clear_redirects.py
```

```bash
./detect_common_cms.py <file with urls>
```

```bash
./detect_server_version.py <file with urls>
```

```bash
./enumerate_wordpress.py <cms.csv> <base directory>
```

```bash
./generate_report.py <base directory> <target domain>
```
