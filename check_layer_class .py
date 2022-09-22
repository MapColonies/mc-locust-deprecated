from utilities.mapproxy_layer import MapproxyLayer

layer1 = MapproxyLayer(layer_id="shay5", zoom=0.0439453125,
                       product_bbox=[35.024411528661574, 32.79419004139809, 35.37597717328861, 32.947998391903226])

print(layer1.get_zoom_range().get_range_value())
print(layer1.get_x_tile_ranges().get_range_value())
print(layer1.get_y_tile_ranges().get_range_value())
