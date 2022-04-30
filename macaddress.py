#!/usr/bin/env python3
import requests
import json
import sys
# import pdb; pdb.set_trace()

# Check the length of the array of command line arguments
if len(sys.argv) <= 1:
  print("macaddress.py <mac address>")
  print("")
  print("Example:")
  print("  macaddress.py 14:7d:da:d9:4d:75")
  exit(0)

# Make an HTTP get request with the first argument as an input variable
request= requests.get(f'https://api.macaddress.io/v1?apiKey=at_Fa2Yfvxp9gHfD2FqoRgdpEkn7by3y&output=json&search={sys.argv[1:2][0]}')

# Print the JSON value with the companyName
print(json.loads(request.text)["vendorDetails"]["companyName"])

# {
#    "vendorDetails":{
#       "oui":"147DDA",
#       "isPrivate":false,
#       "companyName":"Apple, Inc",
#       "companyAddress":"1 Infinite Loop Cupertino CA 95014 US",
#       "countryCode":"US"
#    },
#    "blockDetails":{
#       "blockFound":true,
#       "borderLeft":"147DDA000000",
#       "borderRight":"147DDAFFFFFF",
#       "blockSize":16777216,
#       "assignmentBlockSize":"MA-L",
#       "dateCreated":"2020-04-09",
#       "dateUpdated":"2020-04-09"
#    },
#    "macAddressDetails":{
#       "searchTerm":"14:7d:da:d9:4d:75",
#       "isValid":true,
#       "virtualMachine":"Not detected",
#       "applications":[
         
#       ],
#       "transmissionType":"unicast",
#       "administrationType":"UAA",
#       "wiresharkNotes":"No details",
#       "comment":""
#    }
# }