import logging
import sys
import os

myDir = os.getcwd()
sys.path.append(myDir)
from pathlib import Path

path = Path(myDir)
a = str(path.parent.absolute())
sys.path.append(a)

import requests
from locust import between
from locust import constant
from locust import constant_pacing
from locust import constant_throughput
from locust import HttpUser
from locust import task
from locust_plugins.csvreader import CSVReader
import common.config as cfg
from common import config

logging.error("Reading CSV file")
# pvc_url = cfg.PVC_HANDLER_ROUTE
# response_param = requests.get(url=f'http://{pvc_url}{config.UPDATE_LAYER_DATA_DIR}/',
#                               params={'file': layers_name})
ssn_reader = CSVReader("/home/shayavr/Desktop/git/automation-locust/urls_data.csv")


class MyUser(HttpUser):
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
        wait_time = constant_pacing(int(cfg.WAIT_TIME))
        print("Choosing constant pacing wait time")
    else:
        print("Invalid wait function")

    @task(1)
    def index(self):
        url = next(ssn_reader)
        self.client.get(
            url=url[1]
            , verify=False
        )

    host = cfg.HOST
