#!/bin/bash
for line in $(cat domains.txt); do
	lighthouse http://$line --output json --output-path ./$line.json
done
