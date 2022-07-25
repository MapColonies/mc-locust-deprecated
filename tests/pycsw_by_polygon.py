# ToDo: Shay
# ToDo: Danny

import xmltodict
from common.config import REQUEST_HEADER
from locust import HttpUser, TaskSet, task, between


# ToDo: Add value to the body
ms_polygon_body = r"""<?xml version="1.0" encoding="UTF-8"?>

<csw:GetRecords xmlns:csw="http://www.opengis.net/cat/csw/2.0.2" service="CSW" maxRecords="1" startPosition="1" outputSchema="http://schema.mapcolonies.com/raster" version="2.0.2" xmlns:mc="http://schema.mapcolonies.com/raster" >

<csw:Query typeNames="mc:MCRasterRecord">

<csw:ElementSetName>brief</csw:ElementSetName>

<csw:Constraint version="1.1.0">

<Filter xmlns="http://www.opengis.net/ogc">

<PropertyIsLike wildCard="%" singleChar="_" escapeChar="\\">

<PropertyName>mc:layerPolygonParts</PropertyName>

<Literal>need to add the value</Literal>

</PropertyIsLike>

</Filter>

</csw:Constraint>

</csw:Query>

</csw:GetRecords>
"""



class WebsiteUser(HttpUser):
    wait_time = between(5, 9)

    @task(1)
    def by_polygon(self):
        # ssn_reader
        # start = time.time()
        print("--- running Task")
        print(REQUEST_HEADER)
        # print(xmltodict.parse(ms_id_body))
        response = self.client.post(url="/", data=ms_polygon_body,
                                    headers=REQUEST_HEADER)

        print(response.text)

        # self.client.post(headers=header, xml=ms_id_body)

        # end = time.time()
        # total = end - start
        print('First task..')


