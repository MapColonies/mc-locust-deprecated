from locust import user, task, HttpUser
import common.config as cfg

# Environment variables for XML requests
MC_ID_PROPERTY = cfg.PYCSW_ID_PROPERTY
MC_ID_VALUE = cfg.PYCSW_ID_VALUE
MC_POLYGON_PROPERTY = cfg.PYCSW_POLYGON_PROPERTY
MC_POLYGON_VALUE = cfg.PYCSW_POLYGON_VALUE
MC_REGION_PROPERTY = cfg.PYCSW_REGION_PROPERTY
MC_REGION_VALUE = cfg.PYCSW_REGION_VALUE

# Weights for the different tasks
FIRST_WEIGHT = cfg.FIRST_TASK_WEIGHT
SECOND_TASK_WEIGHT = cfg.SECOND_TASK_WEIGHT
THIRD_TASK_WEIGHT = cfg.THIRD_TASK_WEIGHT
FOURTH_TASK_WEIGHT = cfg.FOURTH_TASK_WEIGHT

# URLs for the relevant tasks
PYCSW_TARGET_URL = cfg.PYCSW_HOST

# Constants for XML post requests
POLYGON_XML = rf"""<?xml version="1.0" encoding="UTF-8"?>

<csw:GetRecords xmlns:csw="http://www.opengis.net/cat/csw/2.0.2" service="CSW" maxRecords="1" startPosition="1" outputSchema="http://schema.mapcolonies.com/raster" version="2.0.2" xmlns:mc="http://schema.mapcolonies.com/raster" >

<csw:Query typeNames="mc:MCRasterRecord">

<csw:ElementSetName>brief</csw:ElementSetName>

<csw:Constraint version="1.1.0">

<Filter xmlns="http://www.opengis.net/ogc">

<PropertyIsLike wildCard="%" singleChar="_" escapeChar="\\">

<PropertyName>{MC_POLYGON_PROPERTY}</PropertyName>

<Literal>{MC_POLYGON_VALUE}</Literal>

</PropertyIsLike>

</Filter>

</csw:Constraint>

</csw:Query>

</csw:GetRecords>
"""


ID_RECORD_XML = rf"""<?xml version="1.0" encoding="UTF-8"?>

<csw:GetRecords xmlns:csw="http://www.opengis.net/cat/csw/2.0.2" service="CSW" maxRecords="1" startPosition="1" outputSchema="http://schema.mapcolonies.com/raster" version="2.0.2" xmlns:mc="http://schema.mapcolonies.com/raster" >

<csw:Query typeNames="mc:MCRasterRecord">

<csw:ElementSetName>brief</csw:ElementSetName>

<csw:Constraint version="1.1.0">

<Filter xmlns="http://www.opengis.net/ogc">

<PropertyIsLike wildCard="%" singleChar="_" escapeChar="\\">

<PropertyName>{MC_ID_PROPERTY}</PropertyName>

<Literal>{MC_ID_VALUE}</Literal>

</PropertyIsLike>

</Filter>

</csw:Constraint>

</csw:Query>

</csw:GetRecords>
"""


REGION_RECORD_XML = rf"""<?xml version="1.0" encoding="UTF-8"?>

<csw:GetRecords xmlns:csw="http://www.opengis.net/cat/csw/2.0.2" service="CSW" maxRecords="1" startPosition="1" outputSchema="http://schema.mapcolonies.com/raster" version="2.0.2" xmlns:mc="http://schema.mapcolonies.com/raster" >

<csw:Query typeNames="mc:MCRasterRecord">

<csw:ElementSetName>brief</csw:ElementSetName>

<csw:Constraint version="1.1.0">

<Filter xmlns="http://www.opengis.net/ogc">

<PropertyIsLike wildCard="%" singleChar="_" escapeChar="\\">

<PropertyName>{MC_REGION_PROPERTY}</PropertyName>

<Literal>{MC_REGION_VALUE}</Literal>

</PropertyIsLike>

</Filter>

</csw:Constraint>

</csw:Query>

</csw:GetRecords>
"""


class SizingUser(HttpUser):
    # wait_time = constant(1)

    @task(1)
    def get_records_by_polygon(self):
        r1 = self.client.post('/', data=POLYGON_XML.encode('utf-8'), headers=cfg.REQUEST_HEADER)
        print(r1.text)
     
     
    @task(2)
    def get_records_by_id(self):
        r2 = self.client.post('/', data=ID_RECORD_XML.encode('utf-8'), headers=cfg.REQUEST_HEADER)
        # print(r2.text)


    @task(3)
    def get_records_by_region(self):
        r3 = self.client.post('/', data=REGION_RECORD_XML.encode('utf-8'), headers=cfg.REQUEST_HEADER)
        # print(r3.text)     

    # @task
    # def get_records_by_bbox(self):
    #     pass
