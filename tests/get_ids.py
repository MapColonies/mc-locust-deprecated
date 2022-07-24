import random
import requests as req
import re
import xmltodict
import os

# todo code review
# todo add random to ids

header = {"x-api-key": os.environ['X-API-KEY']}
csw_url = "https://pycsw-qa-pycsw-nginx-route-raster.apps.v0h0bdx6.eastus.aroapp.io/pycsw/?service=CSW&request" \
          "=GetRecordById&typenames=mc:MCRasterRecord&ElementSetName=full&resultType=results&outputSchema=http" \
          "://schema.mapcolonies.com/raster&version=2.0.2&id="
url_get_ids = r'https://pycsw-qa-pycsw-nginx-route-raster.apps.v0h0bdx6.eastus.aroapp.io/pycsw'
get_id_body = """
<csw:GetRecords xmlns:csw="http://www.opengis.net/cat/csw/2.0.2" service="CSW" maxRecords="5" startPosition="1" resultType="results" outputSchema="http://schema.mapcolonies.com/raster" version="2.0.2" xmlns:mc="http://schema.mapcolonies.com/raster" >

<csw:Query typeNames="mc:MCRasterRecord">

<csw:ElementSetName>full</csw:ElementSetName>

</csw:Query>

</csw:GetRecords>"""


def url_validator(url):
    """ standard validation function that check if provided string is valid url"""
    regex = re.compile(
        r'^(?:http|ftp)s?://'  # http:// or https://
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|'  # domain...
        r'localhost|'  # localhost...
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'  # ...or ip
        r'(?::\d+)?'  # optional port
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)

    return re.match(regex, url) is not None


def get_exception(url, ex, fail=True):
    msg = str(req.exceptions.RequestException(
        "failed on getting response from " + url + "\n error message description: %s" % str(ex)))
    if not fail:
        print(msg)

    else:
        raise print(msg)


def post_request(url, body='', params='', headers=None):
    """
    send post request, and return the response
    """
    url_validator(url)

    try:
        response = req.post(url=url, data=body, headers=headers, params=params)
        return response
    except Exception as ex:
        get_exception(url, ex)


def extract_ids():
    """

    :return: {state: bool, resp: []}
    """
    resp = post_request(url=url_get_ids, body=get_id_body, headers=header)
    if resp.status_code != 200:
        print(f"Failed on post request with status code: {resp.status_code}, and message: {resp.text}")
        return {"state": False, "resp": [resp.text]}
    raw_data = resp.text
    records_ids = []
    csw_dict = xmltodict.parse(raw_data)
    records = csw_dict["csw:GetRecordsResponse"]["csw:SearchResults"]["mc:MCRasterRecord"]
    for record in records:
        for key, value in record.items():
            if key == "mc:id":
                records_ids.append(value)
    return {"state": True, "resp": records_ids}


def check_id(id_list):
    resp_list = []
    if id_list["state"]:
        for id_item in id_list["resp"]:
            response = post_request(url=csw_url+id_item, headers=header)
            resp_list.append(response)
            print("success!")
    return resp_list

