import json
import os

from mc_automation_tools import common

# Files Parameters
WMTS_CSV_PATH = os.environ.get("csv_path", "csv_data/data/wmts_csv_user.csv")
CSV_PATH_3D = os.environ.get("csv_3d_path", "/layerSources/locust_configuration.json")
# WMTS Parameters
LAYER = os.environ.get("layer", "Orthophoto")
LAYER_TYPE = os.environ.get("layer_type", "wmts")
GRIDNAME = os.environ.get("gridName", "newGrids")
VERSION = os.environ.get("version", "2.0.2")
PROJECTION = os.environ.get("projection", "newGrids")
IMAGE_FORMAT = os.environ.get("imageType", ".png")

# PYCSW Parameters)
PYCSW_RECORD_ID = os.environ.get("pycsw_record_id", "mc:id")
PYCSW_COUNTRY_NAME = os.environ.get("pycsw_country_name", "mc:region")
PYCSW_POLYGON = os.environ.get("pycsw_polygon", "mc:layerPolygonParts")
PYCSW_HOST = os.environ.get("pycsw_host", "http://localhost:8000/")

FIRST_TASK_WEIGHT = os.environ.get("first_task_weight", 1)
SECOND_TASK_WEIGHT = os.environ.get("second_task_weight", 2)
THIRD_TASK_WEIGHT = os.environ.get("third_task_weight", 3)
FOURTH_TASK_WEIGHT = os.environ.get("fourth_task_weight", 4)

PYCSW_ID_PROPERTY = os.environ.get("mc_id_property", "mc:id")
PYCSW_REGION_PROPERTY = os.environ.get("mc_region_property", "mc:region")
PYCSW_POLYGON_PROPERTY = os.environ.get("mc_polygon_property", "mc:layerPolygonParts")

PYCSW_ID_VALUE = os.environ.get("mc_id_value", "d53a03e3-650b-4f4e-9047-071667741c08")
PYCSW_REGION_VALUE = os.environ.get("mc_region_value", "string")
PYCSW_POLYGON_VALUE = os.environ.get("mc_polygon_value", "")

# Locust Settings (Parameters)
PORT = os.environ.get("port", "80")
# HOST = os.environ.get(
#     "HOST", "https://pycsw-qa-pycsw-route-raster.apps.v0h0bdx6.eastus.aroapp.io/")

HOST = os.environ.get(
    "HOST",
    "https://mapproxy-raster-qa-mapproxy-route-raster-qa.apps.j1lk3njp.eastus.aroapp.io/api/raster/v1",
)

TOKEN = os.environ.get("SECRET_VALUE_API")
# REQUEST_HEADER = {
#     "X-API-KEY": os.environ.get("SECRET_VALUE_API"),
#     "Content-Type": "text/text; charset=utf-8",
# }
USERS = os.environ.get("users", "15")
SUB_URL = os.environ.get("sub_url_for_pycsw")
# 1 = constant, 2 = constant_throughput, 3 = between, 4 = constant_pacing
WAIT_FUNCTION = int(os.environ.get("wait_function", 4))
MIN_WAIT = int(os.environ.get("min_wait", 1))
MAX_WAIT = int(os.environ.get("max_wait", 1))
WAIT_TIME = int(os.environ.get("wait_time", 1))
# TOKEN = os.environ.get("token","add")
CA_PATH = os.environ.get("ca_path", "/usr/local/share/ca-certificates/ca.crt")
CERT_PATH = os.environ.get("cert_path", "/usr/local/share/ca-certificates/client.crt")
KEY_PATH = os.environ.get("key_path", "/usr/local/share/ca-certificates/client.key")
PRO_ACTIVE_WMTS_BBOX = os.environ.get(
    "pro_active_wmts_bbox",
    [35.024411528661574, 35.79419004139809, 35.37597717328861, 35.947998391903226],
)
# Request Parameters
PARAMS = {
    "service": "CSW",
    "request": "GetRecordById",
    "typenames": "mc:MCRasterRecord",
    "ElementSetName": "full",
    "resultType": "results",
    "outputSchema": "http://schema.mapcolonies.com/raster",
    "version": "2.0.2",
    "id": "3fc674cd-7b77-40ac-8fa3-96b6b4c77f3b",
}

""" connection settings """
PATH_BUILDER = (
    f"{LAYER_TYPE}/{LAYER}/{PROJECTION}/TileMatrix/TileCol/TileRow{IMAGE_FORMAT}"
)

zoom_level_dict = {
    0: 0.703125,
    1: 0.3515625,
    2: 0.17578125,
    3: 0.087890625,
    4: 0.0439453125,
    5: 0.02197265625,
    6: 0.010986328125,
    7: 0.0054931640625,
    8: 0.00274658203125,
    9: 0.001373291015625,
    10: 0.0006866455078125,
    11: 0.00034332275390625,
    12: 0.000171661376953125,
    13: 0.0000858306884765625,
    14: 0.0000429153442382812,
    15: 0.0000214576721191406,
    16: 0.0000107288360595703,
    17: 0.00000536441802978516,
    18: 0.00000268220901489258,
    19: 0.00000134110450744629,
    20: 0.000000670552253723145,
    21: 0.000000335276126861572,
    22: 0.000000167638063430786,
}

CONF_FILE = common.get_environment_variable("CONF_FILE", None)
if not CONF_FILE:
    raise EnvironmentError("Should provide path for CONF_FILE")
try:
    with open(CONF_FILE, "r", encoding="utf-8") as fp:
        conf = json.load(fp)
except Exception as e:
    raise EnvironmentError("Failed to load JSON for configuration") from e

_pg_credentials = conf.get("pg_credential")
PG_USER = _pg_credentials.get("pg_user", None)
PG_PASS = _pg_credentials.get("pg_pass", None)
PG_PORT = _pg_credentials.get("pg_port", None)
PG_HOST = _pg_credentials.get("pg_host", None)
PG_JOB_TASK_DB_NAME = _pg_credentials.get("pg_job_task_table", None)
PG_RECORD_PYCSW_DB = _pg_credentials.get("pg_pycsw_record_table", None)
PG_MAPPROXY_CONFIG = _pg_credentials.get("pg_mapproxy_table", None)
PG_AGENT = _pg_credentials.get("pg_agent_table", None)

_pg_schemas = conf.get("pg_schemas")
DISCRETE_AGENT_DB = _pg_schemas.get("discrete_agent_db")
HEARTBEAT_MANAGER = _pg_schemas.get("heartbeat_manager")
JOB_MANGER = _pg_schemas.get("job_manager")
LAYER_SPEC = _pg_schemas.get("layer_spec")
MAPPROXY_CONFIG = _pg_schemas.get("mapproxy_config")
RASTER_CATALOG = _pg_schemas.get("raster_catalog_manager")
PUBLIC = _pg_schemas.get("public")
LAYERS_LIST = ["test-update", "shay_165", "JAKSHD-2122K-ASDKGBV-4KD4S9X"]

# _pv_routes = conf.get("pvc_routes")
# pvc_root_directory = _pv_routes.get("pvc_root_directory")
