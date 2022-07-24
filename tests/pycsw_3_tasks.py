#ToDo: Danny
from locust import user, task, HttpUser
import common.config as cfg

# Constants for XML post requests
POLYGON_XML = {""}
RECORD_BY_ID_XML = {""}
RECORDS_BY_REGION_XML = {""}

# Weights for the different tasks
FIRST_WEIGHT = cfg.FIRST_TASK_WEIGHT
SECOND_TASK_WEIGHT = cfg.SECOND_TASK_WEIGHT
THIRD_TASK_WEIGHT = cfg.THIRD_TASK_WEIGHT
FOURTH_TASK_WEIGHT = cfg.FOURTH_TASK_WEIGHT

# URLs for the relevant tasks
PYCSW_TARGET_URL = cfg.PYCSW_HOST


class SizingUser(HttpUser):
    # wait_time = constant(1)

    @task(1)
    def get_records_by_polygon(self):

        self.client.post('/', data=POLYGON_XML, headers=cfg.REQUEST_HEADER)

    @task(2)
    def get_records_by_id(self):
        
        self.client.post('/', data=RECORD_BY_ID_XML, headers=cfg.REQUEST_HEADER)

    @task(3)
    def get_records_by_region(self):

        self.client.post('/', data=RECORDS_BY_REGION_XML, headers=cfg.REQUEST_HEADER)

    # @task
    # def get_records_by_bbox(self):
    #     pass
