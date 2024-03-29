import os

from locust import constant
from locust import events
from locust import HttpUser
from locust import tag
from locust import task
from locust import User
from locust_plugins.csvreader import CSVReader

import common.config as cfg

ssn_reader = CSVReader(cfg.requests_file)
print("reading")


@events.init.add_listener
def _(environment, **_kwargs):
    header = os.environ["sub_url_for_pycsw"]
    print(header)


class MyUser(HttpUser):
    wait_time = constant(1)

    @task
    def task1(self):
        self.client.get("/calendar")
        # print(type(ssn_reader))

        points = next(ssn_reader)
        print(points)
        print(os.environ.get("SUB_URL_FOR_IDS"))
