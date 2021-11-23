#!/bin/bash
wpscan -U $2 -P $3 --url $1 -o $4
cat "$4" | sed -n '/Performing password/,$p' | grep '[+]' | tac | sed -n '/Finished:/,$p' | tail -n+2
