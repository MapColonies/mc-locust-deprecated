import mc_automation_tools.postgres
from mc_automation_tools.common import get_environment_variable
from mc_automation_tools import postgres
from typing import List
import config
from mapproxy_layer import MapproxyLayer


def zoom_level_validation(deg_value):
    """
    :param deg_value: float number that presents the resolution deg
        :return: zoom level value : int
        """

    for zoom_level, deg in config.zoom_level_dict.items():
        if deg_value == deg:
            return zoom_level
    return None

def get_layers_list(is_all_records=True) -> dict:
    """
    This method returns layer list for querying
    :return:
    list of layers names
    """
    if not is_all_records:
        try:
            layer_list = get_environment_variable(name=config.LAYERS_LIST)
            if layer_list:
                return {"all_records": is_all_records, "layer_list": layer_list}
        except Exception as e:
            raise e
    return {"all_records": is_all_records, "layer_list": None}


def get_all_layers_tiles_data(db_name=config.PG_RECORD_PYCSW_DB):
    """This method query and return all layer bbox and zoom level values from the records table"""
    client = postgres.PGClass(config.PG_HOST, db_name, config.PG_USER, config.PG_PASS, config.RASTER_CATALOG,
                              port=int(config.PG_PORT))
    columns_names = """
     max_resolution_deg , product_bbox , product_id
    """
    res = client.get_column_by_name(table_name="records", column_name=columns_names)

    return res


def get_layer_list_tile_data(layer_list, db_name=config.PG_RECORD_PYCSW_DB):
    """
    This method return list of costume layer data.
    :param db_name:  db name
    :param layer_list: costume layer data as defined on the configuration file
    :return: layer's resolution_deg, bbox and product_id
    """
    columns_names = """
     max_resolution_deg , product_bbox , product_id
    """
    client = postgres.PGClass(config.PG_HOST, db_name, config.PG_USER, config.PG_PASS, config.RASTER_CATALOG,
                              port=int(config.PG_PORT))
    layers_data_list = []
    for layer_name in layer_list:
        res = client.get_columns_by_pk_equality(columns=columns_names, table_name="records", pk="product_id",
                                                pk_value=layer_name)
        layers_data_list.append(res)
    return layers_data_list


def convert_bbox_str_value_to_string(bbox_value: str) -> list:
    return list(map(float, list(bbox_value.split(","))))


def create_mapproxy_layer_objects(layers_data_list: list) -> list:
    """
    This method gets query results and converts layers data to MapproxyLayer objects
    :param layers_data_list: list of layers data
    :return: list of MapproxyLayer objects
    """
    mapproxy_objects = []

    for layer in layers_data_list:
        layer_bbox = convert_bbox_str_value_to_string(layer[1])
        zoom_deg = layer[0]
        zoom_level = zoom_level_validation(deg_value=zoom_deg)
        if not zoom_level:
            break
        mapproxy_objects.append(MapproxyLayer(zoom=zoom_level, product_bbox=layer_bbox, layer_id=layer[2]))
    return mapproxy_objects


def get_layers_tiles_ranges(layers_data_list: List[MapproxyLayer]) -> list:
    """
    This method gets mapproxy objects and return for each layer the tiles ranges
    :param layers_data_list: list of mapproxy objects
    :return: tiles ranges for each layer :list
    """
    layers_tiles_ranges = []
    for mapproxy_obj in layers_data_list:
        ranges_values = {}
        ranges_values["layer_id"] = mapproxy_obj.get_layer_id
        ranges_values["x_ranges"] = mapproxy_obj.get_x_tile_ranges()
        ranges_values["y_ranges"] = mapproxy_obj.get_y_tile_ranges()
        ranges_values["zoom_ranges"] = mapproxy_obj.get_zoom_range()
        layers_tiles_ranges.append(ranges_values)
    return layers_tiles_ranges


def get_layers_data_pro_active():
    """
    This method returns list of selected layers tiles and zoom ranges for running locust users simulation
    :return:
    layers_tiles_ranges : dict of the layers ids and ranges

    """
    layers_list_res = get_layers_list()
    if layers_list_res["all_records"]:
        layers_tiles_data = get_all_layers_tiles_data()
    else:
        layers_tiles_data = get_layer_list_tile_data(layer_list=layers_list_res["layer_list"])

    mapproxy_objects_list = create_mapproxy_layer_objects(layers_data_list=layers_tiles_data)

    layers_tiles_ranges = get_layers_tiles_ranges(layers_data_list=mapproxy_objects_list)

    return layers_tiles_ranges

