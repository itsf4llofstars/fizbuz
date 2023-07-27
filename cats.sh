#!/usr/bin/env bash
# cats.sh
# A script to print commonly cat'd textfiles
# Works well by adding a symbolic link to ~/bin as
# cats.

printf "%s/\n" "Hello, world! today is: $(date +'%FT%T %:::z')Z - $0" 2>/dev/null

exit 0
