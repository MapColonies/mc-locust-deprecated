import os

# Files Parameters
WMTS_CSV_PARAMS = os.environ.get("csv_path", "csv_data/data/wmts_csv_user.csv")

# WMTS Parameters
layer = os.environ.get("layer", "OrthophotoHistory")
layer_type = os.environ.get("layer_type", "wmts")
gridName = os.environ.get("gridName", "default")
version = os.environ.get("version", "default")
projection = os.environ.get("projection", "newGrids")
image_format = os.environ.get("imageType", "default")

# PYCSW Parameters)
PYCSW_RECORD_ID = os.environ.get('pycsw_record_id')
PYCSW_COUNTRY_NAME = os.environ.get('pycsw_country_name')
PYCSW_POLYGON = os.environ.get('pycsw_polygon')

# Locust Settings (Parameters)
PORT = os.environ.get("port", "80")
HOST = os.environ.get(
    "HOST", "https://pycsw-qa-pycsw-route-raster.apps.v0h0bdx6.eastus.aroapp.io/")
REQUEST_HEADER = {'X-API-KEY': os.environ.get('SECRET_VALUE_API')}
USERS = os.environ.get("users", "15")
SUB_URL = os.environ.get('sub_url_for_pycsw')


# Request Parameters
PARAMS = {'service': 'CSW',
          'request': 'GetRecordById',
          'typenames': 'mc:MCRasterRecord',
          'ElementSetName': 'full',
          'resultType': 'results',
          'outputSchema': 'http://schema.mapcolonies.com/raster',
          'version': '2.0.2',
          'id': '3fc674cd-7b77-40ac-8fa3-96b6b4c77f3b'}

""" connection settings """
path_builder = f"{layer_type}/{layer}/{projection}/TileMatrix/TileCol/TileRow{image_format}"

# runTimeMin = 90
# delayBetweenTileRequests = 100  # ms
# delayBetweencapabilitiesRequests = 0  # ms
# zMin = 0
# zMax = 21


