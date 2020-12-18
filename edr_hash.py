import json
import requests
import getpass
import pprint

from requests.auth import HTTPBasicAuth

username = input('Enter your username: ')
password = getpass.getpass('Enter your password: ')
rest_url = 'https://fortinetdemous.console.ensilo.com/management-rest/hash/search'

file1 = open('ioc.txt', 'r')
hash = [line.rstrip() for line in file1.readlines()]

for line in hash:
    query_hash = {'fileHashes':hash}
    response = requests.get(rest_url, params=query_hash, auth=HTTPBasicAuth(username,password), verify=False)
    json_load = json.loads(response.content)
    pprint.pprint(json_load)

file1.close()
