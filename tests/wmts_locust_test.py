import time
import uuid
import json

import xmltodict
from locust import TaskSet, task, events
from requests import Response
# from tools import GeneralTools
from get_ids import post_request, url_get_ids, get_id_body, header


@events.init.add_listener
def _(environment, **_kwargs):
    print("2. Initializing locust, happens after parsing the locustfile but before test start")


@events.test_start.add_listener
def _(environment, **_kwargs):
    print("test listner")


class ApiTasks(TaskSet):

    def extract_ids(self):
        """

        :return: {state: bool, resp: []}
        """
        resp = post_request(url=url_get_ids, body=get_id_body, headers=header)
        if resp.status_code != 200:
            print(
                f"Failed on post request with status code: {resp.status_code}, and message: {resp.text}")
            return {"state": False, "resp": [resp.text]}
        raw_data = resp.text
        records_ids = []
        csw_dict = xmltodict.parse(raw_data)
        records = csw_dict["csw:GetRecordsResponse"]["csw:SearchResults"]["mc:MCRasterRecord"]
        for record in records:
            for key, value in record.items():
                if key == "mc:id":
                    records_ids.append(value)
        return {"state": True, "resp": records_ids}

    def on_start(self):
        """ on_start is called when a Locust start before any task is scheduled """
        self.response_id_data = self.extract_ids()
        print("on start called")

    def on_stop(self):
        """ on_stop is called when the TaskSet is stopping """

        print("On Stoped called")

    @task(1)
    def FirstTest(self):
        # ssn_reader
        start = time.time()
        print("--- running Task")
        sub_url = "pycsw/?service=CSW&request" \
                  "=GetRecordById&typenames=mc:MCRasterRecord&ElementSetName=full&resultType=results&outputSchema=http"\
                  "://schema.mapcolonies.com/raster&version=2.0.2&id="
        if self.response_id_data["state"]:
            for id_item in self.response_id_data["resp"]:
                self.client.post(url=sub_url + id_item, headers=header)
        end = time.time()
        total = end - start
        print('First task..')
