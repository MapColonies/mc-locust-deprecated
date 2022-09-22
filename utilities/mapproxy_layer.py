from math import floor
from typing import Optional

import config


# ToDo: Fix Typing input and output. v
# ToDo: Add Zoom tuple range -> from 0 to "zoom_level" as tuple
# ToDo: Zoom level convertor -> from deg (check in DB if its only deg) to zoom_level(0-20 dict i sent you in slack) v


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
        self.bbox = product_bbox
        self.zoom = zoom
        self.deg_per_tile = 0.001373

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
    def zoom_level(self) -> float:
        return self.zoom

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
        zoom_level = zoom_level_convertor(deg_value=self.zoom)
        if zoom_level:
            return Range(0, zoom_level)
        return None
