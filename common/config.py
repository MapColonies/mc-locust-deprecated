import os

# Files Parameters
WMTS_CSV_PATH = os.environ.get("csv_path", "csv_data/data/wmts_csv_user.csv")

# WMTS Parameters
LAYER = os.environ.get("layer", "OrthophotoHistory")
LAYER_TYPE = os.environ.get("layer_type", "wmts")
GRIDNAME = os.environ.get("gridName", "default")
VERSION = os.environ.get("version", "2.0.2")
PROJECTION = os.environ.get("projection", "newGrids")
IMAGE_FORMAT = os.environ.get("imageType", ".png")

# PYCSW Parameters)
PYCSW_RECORD_ID = os.environ.get('pycsw_record_id', "mc:id")
PYCSW_COUNTRY_NAME = os.environ.get('pycsw_country_name', "mc:region")
PYCSW_POLYGON = os.environ.get('pycsw_polygon', "mc:layerPolygonParts")

# Locust Settings (Parameters)
PORT = os.environ.get("port", "80")
HOST = os.environ.get(
    "HOST", "https://pycsw-qa-pycsw-route-raster.apps.v0h0bdx6.eastus.aroapp.io/")
REQUEST_HEADER = {'X-API-KEY': os.environ.get('SECRET_VALUE_API')}
USERS = os.environ.get("users", "15")
SUB_URL = os.environ.get('sub_url_for_pycsw')
CONSTANT_THROUGHPUT = os.environ.get('constant_throughput', 1)

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
PATH_BUILDER = f"{LAYER_TYPE}/{LAYER}/{PROJECTION}/TileMatrix/TileCol/TileRow{IMAGE_FORMAT}"

# runTimeMin = 90
# delayBetweenTileRequests = 100  # ms
# delayBetweencapabilitiesRequests = 0  # ms
# zMin = 0
# zMax = 21

