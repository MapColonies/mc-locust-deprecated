#ToDo: Danny
from locust import user, task, HttpUser

# Constants for XML post requests
POLYGON_XML = {""}
RECORD_BY_ID_XML = {""}
RECORDS_BY_REGION_XML = {""}

# Weights for the different tasks
FIRST_TASK_WEIGHT = 1
SECOND_TASK_WEIGHT = 2
THIRD_TASK_WEIGHT = 3
FOURTH_TASK_WEIGHT = 4

# URLs for the relevant tasks
PYCSW_TARGET_URL = ""


class SizingUser(HttpUser):
    # wait_time = constant(1)

    @task(1)
    def get_records_by_polygon(self):

        self.client.post('/post', data=POLYGON_XML)

    @task(2)
    def get_records_by_id(self):

        self.client.post('/post', data=RECORD_BY_ID_XML)

    @task(3)
    def get_records_by_region(self):

        self.client.post('/post', data=RECORDS_BY_REGION_XML)

    # @task
    # def get_records_by_bbox(self):
    #     pass
