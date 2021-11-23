#!/bin/bash

mkdir -p $2/wordpress
wpscan -e u -o "$2/wordpress/$3.txt" --url $1
cat "$2/wordpress/$3.txt" | sed -n '/User(s) Identified:/,$p' | grep '[+]' | tac | sed -n '/Finished:/,$p' | tail -n+2 | cut -d' ' -f2
