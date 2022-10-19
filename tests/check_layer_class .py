from common.config import PRO_ACTIVE_WMTS_BBOX
from utilities.mapproxy_layer import MapproxyLayer

layer1 = MapproxyLayer(
    layer_id="shay5", zoom=0.0439453125, product_bbox=PRO_ACTIVE_WMTS_BBOX
)

# print(layer1.get_zoom_range().get_range_value())
# print(layer1.get_x_tile_ranges().get_range_value())
# print(layer1.get_y_tile_ranges().get_range_value())
