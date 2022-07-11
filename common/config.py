import os
# import common.auth

""" CSV """
requests_file = "wmts_csv_user.csv"

# test settings
layer = os.environ.get("layer")
gridName = os.environ.get("gridName")
version = "1.0.0"
projection = os.environ.get("projection")
image_format = os.environ.get("imageType")
users = 25

runTimeMin = 90
delayBetweenTileRequests = 100  # ms
delayBetweencapabilitiesRequests = 0  # ms

zMin = 0
zMax = 21
""" connection settings """
layer_type = os.environ.get("layer_type")
path_builder = f"{layer_type}/{layer}/{projection}/TileMatrix/TileCol/TileRow{image_format}"

HOST = "https://pycsw-qa-pycsw-route-raster.apps.v0h0bdx6.eastus.aroapp.io/"
PORT = 80
REQUEST_HEADER = {'X-API-KEY': os.environ.get('SECRET_VALUE_API')}
PARAMS = {'service': 'CSW',
          'request': 'GetRecordById',
          'typenames': 'mc:MCRasterRecord',
          'ElementSetName': 'full',
          'resultType': 'results',
          'outputSchema': 'http://schema.mapcolonies.com/raster',
          'version': '2.0.2',
          'id': '3fc674cd-7b77-40ac-8fa3-96b6b4c77f3b'}

SUB_URL = os.environ.get('SUB_URL_FOR_IDS')
