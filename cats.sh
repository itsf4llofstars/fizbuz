#!/usr/bin/env bash

HOMEDIR=/home/"$USER"
PWD=$pwd

clear

printf "\n\n\n"
printf "\t%s\n" "Select your file:"
printf "\t\t%s\n" "1. gnome terminal"
printf "\t\t%s\n" "2. terminator"

echo
printf "\t\t%s" "Choice: "
read choice

clear

cd "$HOMEDIR"/bashscripts/commoncats || exit 1

case $choice in
    1)
        cat gnome.txt
        ;;
    2)
        cat terminator.txt
        ;;
    *)
        printf "\n%s\n\n" "No entry selected"
        ;;
esac

cd "$PWD" || exit

exit 0
