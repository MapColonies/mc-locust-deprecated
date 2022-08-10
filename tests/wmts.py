from locust import HttpUser, task, constant_throughput , constant, between, constant_pacing
from locust_plugins import StopUser
from locust_plugins.csvreader import CSVReader
import common.config as cfg
import time
import logging

logging.error("Reading CSV file")
ssn_reader = CSVReader("csv_data/data/wmts_csv_user.csv")


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
        wait_time = constant_pacing(cfg.WAIT_TIME)
        print("Choosing constant pacing wait time")
    else:
        print("Invalid wait function")

    @task(1)
    def index(self):
        points = next(ssn_reader)
        # self.client.get(

        #     f"/wmts/2022_04_04T12_01_48Z_MAS_6_ORT_247557-Orthophoto/newGrids/1/0/1.png",
        #     headers=cfg.default_headers)
        # print(
        #     f"/wmts/2022_04_04T12_01_48Z_MAS_6_ORT_247557-Orthophoto/newGrids/1/0/1.png")
        self.client.get(f"/{cfg.LAYER_TYPE}/{cfg.LAYER}/{cfg.GRIDNAME}/{points[0]}/{points[1]}/{points[2]}{cfg.IMAGE_FORMAT}",
                        headers=cfg.REQUEST_HEADER)
        # print(
        #     f"/{cfg.layer_type}/{cfg.layer}/{cfg.projection}/{points[0]}/{points[1]}/{points[2]}{cfg.image_format}")
        # print(customer)

    host = cfg.HOST
