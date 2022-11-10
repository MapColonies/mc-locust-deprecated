import logging
import time
from locust import between
from locust import constant
from locust import constant_pacing
from locust import constant_throughput
from locust import HttpUser
from locust import task
from locust_plugins import StopUser
from locust_plugins.csvreader import CSVReader

import common.config as cfg
from utilities.get_all_layer import get_layers_data_pro_active

logging.error("Reading CSV file")
ssn_reader = CSVReader("csv_data/data/wmts_shaziri.csv")


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

    def on_start(self):
        self.layers_tiles_ranges = get_layers_data_pro_active()

    @task(1)
    def index(self):
        points = next(ssn_reader)
        self.layers_tiles_ranges
        self.client.get(
            f"/{cfg.LAYER_TYPE}/{cfg.LAYER}/{cfg.GRIDNAME}/{points[0]}/{points[1]}/{points[2]}{cfg.IMAGE_FORMAT}?token={cfg.TOKEN}"
            , verify=False
        )

    # with self.client.get(
    #       f"/{cfg.LAYER_TYPE}/{cfg.LAYER}/{cfg.GRIDNAME}/{points[0]}/{points[1]}/{points[2]}{cfg.IMAGE_FORMAT}?
    #       # ,verify=False,
    #   ) as response:
    #       if response.text != "Success":
    #           print("continue")
    host = cfg.HOST
