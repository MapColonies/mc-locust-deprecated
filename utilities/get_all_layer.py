import mc_automation_tools.postgres
from mc_automation_tools import postgres
import config


def get_all_layers_tiles_data (db_name=config.PG_RECORD_PYCSW_DB):
    """This method query and return all layer bbox and zoom level values from the records table"""
    client = postgres.PGClass(config.PG_HOST, db_name, config.PG_USER, config.PG_PASS, config.RASTER_CATALOG,
                              port=int(config.PG_PORT))
    columns_names = """
     max_resolution_deg , product_bbox , product_id
    """
    res = client.get_column_by_name(table_name="records", column_name=columns_names)
    print(res)

    return res


get_all_layers_tiles_data()