from mc_automation_tools import common
import json

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


