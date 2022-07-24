import os
# import common.auth

""" CSV """
requests_file = os.environ.get("csv_path","csv_data/data/wmts_csv_user.csv")

# test settings
layer = os.environ.get("layer", "OrthophotoHistory")
gridName = os.environ.get("gridName", "default")
version = os.environ.get("version", "default")
projection = os.environ.get("projection", "newGrids")
image_format = os.environ.get("imageType", "default")
users = os.environ.get("users")

""" connection settings """
layer_type = os.environ.get("layer_type","wmts")
path_builder = f"{layer_type}/{layer}/{projection}/TileMatrix/TileCol/TileRow{image_format}"
#ToDo: Fix host for enviroment
HOST = "https://pycsw-qa-pycsw-route-raster.apps.v0h0bdx6.eastus.aroapp.io/"
PORT = os.environ.get("port", "80")
REQUEST_HEADER = {'X-API-KEY': os.environ.get('SECRET_VALUE_API')}
PARAMS = {'service': 'CSW',
          'request': 'GetRecordById',
          'typenames': 'mc:MCRasterRecord',
          'ElementSetName': 'full',
          'resultType': 'results',
          'outputSchema': 'http://schema.mapcolonies.com/raster',
          'version': '2.0.2',
          'id': '3fc674cd-7b77-40ac-8fa3-96b6b4c77f3b'}

SUB_URL = os.environ.get('sub_url_for_pycsw')
PYCSW_RECORD_ID = os.environ.get('pycsw_record_id')
PYCSW_COUNTRY_NAME = os.environ.get('pycsw_country_name')
PYCSW_POLYGON = os.environ.get('pycsw_polygon')
# runTimeMin = 90
# delayBetweenTileRequests = 100  # ms
# delayBetweencapabilitiesRequests = 0  # ms
# zMin = 0
# zMax = 21