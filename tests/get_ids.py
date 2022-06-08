import requests as req
import re
import xml.etree.ElementTree as ET


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


def post_request(url, body='', params='', headers=''):
    """
    send post request, and return the response
    """
    url_validator(url)

    try:
        response = req.post(url=url, data=body, headers=headers, params=params)
        if response.status_code == 200:
            return response.content

    except Exception as ex:
        get_exception(url, ex)


def extract_ids(response_content, xmlns_adress):
    ids = []
    tree = response_content
    root = tree.getroot()
    ET.register_namespace("", xmlns_adress)

    for subnet in root.iter(f'{xmlns_adress}mc:id'):
        print(subnet.text)
        ids.append(subnet.text)

    return ids

def check_id( ids_array):
    for id in ids_array:
        requests_url = f"url={id}" #send id to the url address

















# tree = ET.parse('csr1kv_file.xml')
# root = tree.getroot()
# ET.register_namespace("", "http://www.test.com/esc/esc")
#
# for subnet in root.iter('address'):
#     print(subnet)
