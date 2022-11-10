from typing import Iterable
from itertools import product
import config as cfg


def xml_builder_job():
    # Return XML string after building it from the template.
    # ToDO: Shay change all relevant values
    XML_BODY = f"""
    <?xml version="1.0" encoding="UTF-8"?>
<csw:GetRecords xmlns:csw="http://www.opengis.net/cat/csw/2.0.2" service="CSW" maxRecords="1"  startPosition="1"  outputSchema="http://schema.mapcolonies.com/raster" version="2.0.2" xmlns:mc="http://schema.mapcolonies.com/raster" >
  <csw:Query typeNames={cfg.HOST}>
   <csw:ElementSetName>brief</csw:ElementSetName>
    <csw:Constraint version="1.1.0">
      <Filter xmlns="http://www.opengis.net/ogc">
        <PropertyIsLike wildCard="%" singleChar="_" escapeChar="\\">
          <PropertyName>mc:id</PropertyName>
          <Literal>d53a03e3-650b-4f4e-9047-071667741c08</Literal>
        </PropertyIsLike>
      </Filter>
    </csw:Constraint>
  </csw:Query>
</csw:GetRecords>
"""
    return XML_BODY


class WMTSIterator:
    "WMTSIterator - with range"

    def __init__(self, range_: range):
        self.points = iter(range_)
        self.range = range_

    def __next__(self) -> Iterable[int]:
        try:
            return next(self.points)
        except StopIteration:
            self.points = iter(self.range)
            return next(self.points)


def wmts_url_builder(x_val, y_val, zoom_val):
    """
    This method build the url of given tile parameters
    :return:
    wmts_url: url of the given layer's tile
    """
    wmts_url = f"/{cfg.LAYER_TYPE}/{cfg.LAYER}/{cfg.GRIDNAME}/{x_val}/{y_val}/{zoom_val}{cfg.IMAGE_FORMAT}?token={cfg.TOKEN}"
    return wmts_url


# def create_tiles_url_order(zoom_ranges, x_ranges, y_ranges):
#     """
#     This method create possible tiles order based on range's value
#     :param zoom_ranges: zoom ranges value
#     :param x_ranges: x ranges value
#     :param y_ranges: y ranges value
#
#     :return: tiles combination
#     """
#     x_values = [*range(x_ranges[0], x_ranges[1] + 1)]
#     y_values = [*range(y_ranges[0], y_ranges[1] + 1)]
#     zoom_values = [*range(zoom_ranges[0], zoom_ranges[1] + 1)]
#     return list(product(zoom_values, x_values, y_values))
#
#
# print(create_tiles_url_order([0, 4], [5, 6], [19, 20]))


def create_tiles_url_order(zoom_ranges, x_ranges, y_ranges):
    """
    This method create possible tiles order based on range's value
    :param zoom_ranges: zoom ranges value
    :param x_ranges: x ranges value
    :param y_ranges: y ranges value"""
    tiles_lst = []
    x_values = [*range(x_ranges[0], x_ranges[1] + 1)]
    y_values = [*range(y_ranges[0], y_ranges[1] + 1)]
    zoom_values = [*range(zoom_ranges[0], zoom_ranges[1] + 1)]
    print(list(product(zoom_values, y_values, x_values)))
    print(len(list(product(zoom_values, y_values, x_values))))
    return list(product(zoom_values, y_values, x_values))


create_tiles_url_order([0, 4], [5, 6], [19, 20])
# class WMTSIterator():
# "WMTSIterator - without range"
#     def __init__(self, start_index, end_index):
#         self.start = start_index
#         self.end = end_index
#         self.points = iter(range(start_index, end_index))

#     def __next__(self):
#         try:
#             return next(self.points)
#         except StopIteration:
#             self.points = iter(range(self.start, self.end))
#             return next(self.points)

import glob, os
filelist = glob.glob('D:\Train\*.jpg')
print(len(filelist))
for file in filelist:
    print(file)