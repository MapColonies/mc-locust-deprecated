from math import floor


class Range:
    def __init__(self, min_val, max_val):
        self.min_val = min_val
        self.max_val = max_val
        self.range = self.get_range_value()

    def get_range_value(self):
        return (self.min_val, self.max_val)


class MapproxyLayer:
    def __init__(self, layer_id, zoom, product_bbox):
        self.layer_id = layer_id
        self.bbox = product_bbox
        self.zoom = zoom
        self.deg_per_tile = 0.001373

    @property
    def minx_deg(self):
        return self.bbox[0]

    @property
    def miny_deg(self):
        return self.bbox[1]

    @property
    def maxx_deg(self):
        return self.bbox[2]

    @property
    def maxy_deg(self):
        return self.bbox[3]

    @property
    def zoom_level(self):
        return self.zoom

    def get_x_tile_ranges(self):
        min_tile_x = floor((self.minx_deg + 180) / self.deg_per_tile, 1)
        max_tile_x = floor((self.maxx_deg + 180) / self.deg_per_tile, 1) + 1
        return Range(min_tile_x, max_tile_x)

    def get_y_tile_ranges(self):
        min_tile_y = pow(2, self.zoom_level) - floor((self.maxy_deg + 90) / self.deg_per_tile, 1) - 1
        max_tile_y = pow(2, self.zoom_level) - floor((self.miny_deg + 90) / self.deg_per_tile, 1)
        return Range(min_tile_y, max_tile_y)
