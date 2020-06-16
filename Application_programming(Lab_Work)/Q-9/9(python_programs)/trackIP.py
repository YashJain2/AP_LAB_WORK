import os

from urllib.request import urlopen

import json

while True:
    ip=input("What is traget IP address :")
    url="http://ip-api.com/json/"
    response=urlopen(url+ip)
    data=response.read()
    values=json.loads(data)

    print("IP : "+values['query'])
    print("city : "+values['city'])
    print("ISP :"+values['isp'])
    print("Country :"+values['country'])
    print("region :"+values['region'])
    print("Timezone :"+values['timezone'])

    break
