#4. Write a program that takes a URL as a command-line argument and reports
# whether or not there is a working website at that address.
import sys
import requests
tag = sys.argv[1]

url = 'http://' + tag

resp = requests.get(url)

print(url)