#!/usr/bin/env bash
# cats.sh
# A script to print commonly cat'd textfiles

printf "%s/\n" "Hello, world! today is: $(date +'%FT%T %:::z')Z - $0" 2>/dev/null

exit 0
