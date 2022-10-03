import os
import time

from locust import HttpUser
from locust import task
from locust import TaskSet

from playground.get_ids import extract_ids
from playground.get_ids import header


class UserBehaviour(HttpUser):
    # wait_time = 1
    response_id_data = ""

    # @task(1)
    # def index(self):
    #     start = time.time()
    #     print("--- running Task")
    #     sub_url = "pycsw/?service=CSW&request" \
    #       "=GetRecordById&typenames=mc:MCRasterRecord&ElementSetName=full&resultType=results&outputSchema=http" \
    #       "://schema.mapcolonies.com/raster&version=2.0.2&id="
    #     if self.response_id_data["state"]:
    #
    #         for id_item in self.response_id_data["resp"]:
    #             print(sub_url+id_item)
    #             self.client.post(url=sub_url+id_item, headers=header)
    #     # check_id(self.response_id_data)
    #     end = time.time()
    #     total = end - start

    @task(1)
    def index(self):
        # start = time.time()
        # print("--- running Task")
        # sub_url = "pycsw/?service=CSW&request" \
        #     "=GetRecordById&typenames=mc:MCRasterRecord&ElementSetName=full&resultType=results&outputSchema=http" \
        #     "://schema.mapcolonies.com/raster&version=2.0.2&id="
        sub_url = os.environ["SUB_URL"]
        if self.response_id_data["state"]:
            for id_item in self.response_id_data["resp"]:

                self.client.post(url=sub_url + id_item, headers=header)
        # end = time.time()
        # total = end - start

    def get_id_data(self):
        self.response_id_data = extract_ids()
        print(self.response_id_data)

    def on_start(self):
        self.extract_ids()
