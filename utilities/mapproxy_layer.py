import config
from math import floor
from typing import Optional


def zoom_level_convertor(deg_value: float) -> Optional[int]:
    """

    :param deg_value: float number that presents the resolution deg
    :return: zoom level value : int
    """
    for zoom_level, deg in config.zoom_level_dict.items():
        if deg_value == deg:
            return zoom_level
    return None


class Range:
    def __init__(self, min_val: int, max_val: int):
        self.min_val = min_val
        self.max_val = max_val
        self.range = self.get_range_value()

    def get_range_value(self):
        return self.min_val, self.max_val


class MapproxyLayer:
    def __init__(self, layer_id: str, zoom: float, product_bbox: list):
        self.layer_id = layer_id
        self.zoom_deg = zoom
        self.bbox = product_bbox


    @property
    def min_x_deg(self) -> float:
        return self.bbox[0]

    @property
    def min_y_deg(self) -> float:
        return self.bbox[1]

    @property
    def max_x_deg(self) -> float:
        return self.bbox[2]

    @property
    def max_y_deg(self) -> float:
        return self.bbox[3]

    @property
    def zoom_level(self) -> int:
        return zoom_level_convertor(deg_value=self.zoom_deg)

    @property
    def deg_per_tile(self):
        return self.get_deg_per_tile(zoom_level=self.zoom_level)

    def get_x_tile_ranges(self) -> Range:
        min_tile_x = floor((self.min_x_deg + 180) / self.deg_per_tile)
        max_tile_x = floor((self.max_x_deg + 180) / self.deg_per_tile) + 1
        return Range(min_tile_x, max_tile_x)

    def get_y_tile_ranges(self) -> Range:
        min_tile_y = pow(2, self.zoom_level) - \
                     floor((self.max_y_deg + 90) / self.deg_per_tile) - 1
        max_tile_y = pow(2, self.zoom_level) - \
                     floor((self.min_y_deg + 90) / self.deg_per_tile)
        return Range(min_tile_y, max_tile_y)

    def get_zoom_range(self) -> Optional[Range]:
        zoom_level = zoom_level_convertor(deg_value=self.zoom_deg)
        if zoom_level:
            return Range(0, zoom_level)
        return None

    def get_deg_per_tile(self, zoom_level: int):
        deg_per_tile = 180 / pow(2, zoom_level)
        return deg_per_tile

# usage example
x = MapproxyLayer("shay7", 0.0439453125, [35.024411528661574, 32.79419004139809, 35.37597717328861, 32.947998391903226])
print(x.get_x_tile_ranges().range)
print(x.get_y_tile_ranges().range)
print(x.get_zoom_range().range)
