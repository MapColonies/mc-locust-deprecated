from common.config import REQUEST_HEADER
from locust import HttpUser, TaskSet, task, between

RECORDS_BY_REGION_XML = r"""<?xml version="1.0" encoding="UTF-8"?>

<csw:GetRecords xmlns:csw="http://www.opengis.net/cat/csw/2.0.2" service="CSW" maxRecords="1" startPosition="1" outputSchema="http://schema.mapcolonies.com/raster" version="2.0.2" xmlns:mc="http://schema.mapcolonies.com/raster" >

<csw:Query typeNames="mc:MCRasterRecord">

<csw:ElementSetName>brief</csw:ElementSetName>

<csw:Constraint version="1.1.0">

<Filter xmlns="http://www.opengis.net/ogc">

<PropertyIsLike wildCard="%" singleChar="_" escapeChar="\\">

<PropertyName>mc:region</PropertyName>

<Literal>ישראל</Literal>

</PropertyIsLike>

</Filter>

</csw:Constraint>

</csw:Query>

</csw:GetRecords>
"""

class WebsiteUser(HttpUser):
    # wait_time = between(5, 9)

    @task(1)
    def by_id(self):
        response = self.client.post(url="/", data=RECORDS_BY_REGION_XML.encode('utf-8'),
                                    headers=REQUEST_HEADER)

        print(response.text)
