from bson import encode
from locust import between
from locust import constant
from locust import constant_pacing
from locust import constant_throughput
from locust import HttpUser
from locust import task
from locust import user

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

    if cfg.WAIT_FUNCTION == 1:
        wait_time = constant(cfg.WAIT_TIME)
        print("Choosing constant wait time")
    elif cfg.WAIT_FUNCTION == 2:
        wait_time = constant_throughput(cfg.WAIT_TIME)
        print("Choosing constant throughput wait time")
    elif cfg.WAIT_FUNCTION == 3:
        wait_time = between(cfg.MIN_WAIT, cfg.MAX_WAIT)
        print("Choosing between wait time")
    elif cfg.WAIT_FUNCTION == 4:
        wait_time = constant_pacing(cfg.WAIT_TIME)
        print("Choosing constant pacing wait time")
    else:
        print("Invalid wait function")

    # wait_time = constant_throughput(1)
    # wait_time = between(cfg.MIN_WAIT, cfg.MAX_WAIT)
    # wait_time = constant_pacing(1) # Works bes

    @task(1)
    def get_records_by_polygon(self):
        r1 = self.client.post(
            "/",
            data=POLYGON_XML.encode("UTF-8"),
            # headers=cfg.REQUEST_HEADER,
            verify=cfg.CA_PATH,
        )

    @task(1)
    def get_records_by_id(self):
        r2 = self.client.post(
            "/",
            data=ID_RECORD_XML.encode("utf-8"),
            # headers=cfg.REQUEST_HEADER,
            verify=cfg.CA_PATH,
        )

    @task(1)
    def get_records_by_region(self):
        r3 = self.client.post(
            "/",
            data=REGION_RECORD_XML.encode("utf-8"),
            # headers=cfg.REQUEST_HEADER,
            verify=cfg.CA_PATH,
        )

    # @task
    # def get_records_by_bbox(self):
    #     pass
