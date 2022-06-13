import os
import requests
import xmltodict
from xml.etree import ElementTree
import json
from common.config import REQUEST_HEADER, PARAMS, PORT, HOST

url = 'https://pycsw-qa-pycsw-nginx-route-raster.apps.v0h0bdx6.eastus.aroapp.io/pycsw'
body = """
<csw:GetRecords xmlns:csw="http://www.opengis.net/cat/csw/2.0.2" service="CSW" maxRecords="5"  startPosition="1" resultType="results"  outputSchema="http://schema.mapcolonies.com/raster" version="2.0.2" xmlns:mc="http://schema.mapcolonies.com/raster" >
  <csw:Query typeNames="mc:MCRasterRecord">
   <csw:ElementSetName>full</csw:ElementSetName>
  </csw:Query>
</csw:GetRecords>
"""
hears = {'x-api-key' : 'replace_me'}
# response = requests.get(url=url, params=PARAMS, headers=REQUEST_HEADER)
# o = xmltodict.parse(response.text)
# print(HOST)
# print(o)
response = requests.post(url=url, headers=hears, data=body)
o = xmltodict.parse(response.text)
x = (o['csw:GetRecordsResponse'])
#print(o[''])
print(x)
# print(os.environ.get('DOMAIN'))
# print(os.environ.get('ROOT_URL'))
# print(os.environ.get('DEFAULT_HEADERS'))
