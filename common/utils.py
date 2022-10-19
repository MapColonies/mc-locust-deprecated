from typing import Iterable

import js2py

import config as cfg


def execute_js_code(js_code):
    js = str(js_code).replace("document.write", "return ")
    return js2py.eval_js(js)


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


# class WMTSIterator():
"WMTSIterator - without range"
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
