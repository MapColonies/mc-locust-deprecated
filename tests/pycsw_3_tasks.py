#ToDo: Danny
from locust import user, task, HttpUser
import common.config as cfg
from xml.etree.ElementTree import XML, fromstring
# Constants for XML post requests
POLYGON_XML = """
<?xml version="1.0" encoding="UTF-8"?>
<csw:GetRecords xmlns:csw="http://www.opengis.net/cat/csw/2.0.2" service="CSW" maxRecords="1"  startPosition="1"  outputSchema="http://schema.mapcolonies.com/raster" version="2.0.2" xmlns:mc="http://schema.mapcolonies.com/raster" >
  <csw:Query typeNames="mc:MCRasterRecord">
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
RECORD_BY_ID_XML = """
<?xml version="1.0" encoding="UTF-8"?>
<csw:GetRecords xmlns:csw="http://www.opengis.net/cat/csw/2.0.2" service="CSW" maxRecords="1"  startPosition="1"  outputSchema="http://schema.mapcolonies.com/raster" version="2.0.2" xmlns:mc="http://schema.mapcolonies.com/raster" >
  <csw:Query typeNames="mc:MCRasterRecord">
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
RECORDS_BY_REGION_XML = """
<?xml version="1.0" encoding="UTF-8"?>
<csw:GetRecords xmlns:csw="http://www.opengis.net/cat/csw/2.0.2" service="CSW" maxRecords="1"  startPosition="1"  outputSchema="http://schema.mapcolonies.com/raster" version="2.0.2" xmlns:mc="http://schema.mapcolonies.com/raster" >
  <csw:Query typeNames="mc:MCRasterRecord">
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

# Weights for the different tasks
FIRST_WEIGHT = cfg.FIRST_TASK_WEIGHT
SECOND_TASK_WEIGHT = cfg.SECOND_TASK_WEIGHT
THIRD_TASK_WEIGHT = cfg.THIRD_TASK_WEIGHT
FOURTH_TASK_WEIGHT = cfg.FOURTH_TASK_WEIGHT

# URLs for the relevant tasks
PYCSW_TARGET_URL = cfg.PYCSW_HOST

REQUEST_HEADER = {"x-api-key": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwiZCI6WyJyYXN0ZXIiLCJkZW0iLCJ2ZWN0b3IiLCIzZCJdLCJyZXNvdXJjZVR5cGVzIjpbInJhc3RlciIsImRlbSIsInZlY3RvciIsIjNkIl0sImlhdCI6MTUxNjIzOTAyMn0.PUIHPDNGU3Ji2AB2tMWnwH_BjOaHoEUeZF45mJ8h8GU",
                  "Content-Type" : "application/xml"}


class SizingUser(HttpUser):
    # wait_time = constant(1)

    @task(1)
    def get_records_by_polygon(self):
        # with open('/home/dimitry/Desktop/Automation/automation-locust/tests/request_data.xml', 'r') as xml_fh:
        #     xml_data = xml_fh.read()
        
        myxml = fromstring(POLYGON_XML)
        r1 = self.client.post('/', data=myxml, headers=REQUEST_HEADER)
        print(r1.text)

    # @task(2)
    # def get_records_by_id(self):

    #     r2 = self.client.post('/', data=RECORD_BY_ID_XML,
    #                           headers=REQUEST_HEADER)
    #     print(r2.text)

    # @task(3)
    # def get_records_by_region(self):

    #     self.client.post('/', data=RECORDS_BY_REGION_XML,
    #                      headers=REQUEST_HEADER)

    # @task
    # def get_records_by_bbox(self):
    #     pass
