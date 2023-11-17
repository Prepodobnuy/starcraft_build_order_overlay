#!/usr/bin/expect -f

PASSWORD=$(zenity --password --title="Enter your sudo password")

echo "${PASSWORD}" | sudo -S python3 main.py
