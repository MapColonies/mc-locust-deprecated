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
PYCSW_HOST = os.environ.get('pycsw_host', "http://localhost:8000/")

FIRST_TASK_WEIGHT = os.environ.get('first_task_weight', 1)
SECOND_TASK_WEIGHT = os.environ.get('second_task_weight', 2)
THIRD_TASK_WEIGHT = os.environ.get('third_task_weight', 3)
FOURTH_TASK_WEIGHT = os.environ.get('fourth_task_weight', 4)

PYCSW_ID_PROPERTY = os.environ.get('mc_id_property', "mc:id")
PYCSW_REGION_PROPERTY = os.environ.get('mc_region_property', "mc:region")
PYCSW_POLYGON_PROPERTY = os.environ.get('mc_polygon_property', "mc:layerPolygonParts")

PYCSW_ID_VALUE = os.environ.get('mc_id_value', "d53a03e3-650b-4f4e-9047-071667741c08")
PYCSW_REGION_VALUE = os.environ.get('mc_region_value', "string")
PYCSW_POLYGON_VALUE = os.environ.get('mc_polygon_value', "")


# Locust Settings (Parameters)
PORT = os.environ.get("port", "80")
HOST = os.environ.get(
    "HOST", "https://pycsw-qa-pycsw-route-raster.apps.v0h0bdx6.eastus.aroapp.io/")
REQUEST_HEADER = {'X-API-KEY': os.environ.get('SECRET_VALUE_API'),'Content-Type': 'text/text; charset=utf-8'}
USERS = os.environ.get("users", "15")
SUB_URL = os.environ.get('sub_url_for_pycsw')
WAIT_FUNCTION = os.environ.get('wait_function', 4) # 1 = constant, 2 = constant_throughput, 3 = between, 4 = constant_pacing
MIN_WAIT = os.environ.get('min_wait', 1)
MAX_WAIT = os.environ.get('max_wait', 1)
WAIT_TIME = os.environ.get('wait_time', 1)
CA_PATH = os.environ.get("ca_path", "/usr/local/share/ca-certificates/ca.crt")
CERT_PATH = os.environ.get("cert_path", "/usr/local/share/ca-certificates/client.crt")
KEY_PATH = os.environ.get("key_path", "/usr/local/share/ca-certificates/client.key")

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


