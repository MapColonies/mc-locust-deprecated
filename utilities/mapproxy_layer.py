from math import floor
import typing

# ToDo: Fix Typing input and output.
# ToDo: Add Zoom tuple range -> from 0 to "zoom_level" as tuple
# ToDo: Zoom level convertor -> from deg (check in DB if its only deg) to zoom_level(0-20 dict i sent you in slack)

class Range:
    def __init__(self, min_val, max_val):
        self.min_val = min_val
        self.max_val = max_val
        self.range = self.get_range_value()

    def get_range_value(self):
        return (self.min_val, self.max_val)


class MapproxyLayer():
    def __init__(self, layer_id, zoom, product_bbox):
        self.layer_id = layer_id
        self.bbox = product_bbox
        self.zoom = zoom
        self.deg_per_tile = 0.001373

    @property
    def min_x_deg(self):
        return self.bbox[0]

    @property
    def min_y_deg(self):
        return self.bbox[1]

    @property
    def max_x_deg(self):
        return self.bbox[2]

    @property
    def max_y_deg(self):
        return self.bbox[3]

    @property
    def zoom_level(self):
        return self.zoom

    def get_x_tile_ranges(self):
        min_tile_x = floor((self.min_x_deg + 180) / self.deg_per_tile, 1)
        max_tile_x = floor((self.max_x_deg + 180) / self.deg_per_tile, 1) + 1
        return Range(min_tile_x, max_tile_x)

    def get_y_tile_ranges(self):
        min_tile_y = pow(2, self.zoom_level) - \
            floor((self.max_y_deg + 90) / self.deg_per_tile, 1) - 1
        max_tile_y = pow(2, self.zoom_level) - \
            floor((self.min_y_deg + 90) / self.deg_per_tile, 1)
        return Range(min_tile_y, max_tile_y)
