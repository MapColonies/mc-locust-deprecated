from locust import FastHttpUser, task, between
from playground.temp_lib.op import choose_random_page
import common.config as cfg
import os
from csv_data.manipulation import do_something
from locust_plugins.csvreader import CSVReader
from locust import constant_throughput

runner_url_list = do_something()
# ssn_reader = CSVReader("csv_data/data/wmts_csv_user.csv")
#ToDo: Change the CSVReader from Constant to config name
ssn_reader = CSVReader("csv_data/data/wmts_csv_user.csv")


class MyUser(FastHttpUser):
    wait_time = constant_throughput(1)

    # print(os.environ.get('SECRET_VALUE_API'))
    @task
    def index(self):
        # pass
        # danny comment
        points = next(ssn_reader)
        # print(points)
        # self.client.get(
        #     f"/wmts/2022_04_04T12_01_48Z_MAS_6_ORT_247557-Orthophoto/newGrids/1/0/1.png",
        #     headers=cfg.default_headers)
        # print(
        #     f"/wmts/2022_04_04T12_01_48Z_MAS_6_ORT_247557-Orthophoto/newGrids/1/0/1.png")
        self.client.get(
            f"/{cfg.layer_type}/{cfg.layer}/{cfg.projection}/{points[0]}/{points[1]}/{points[2]}{cfg.image_format}",
            headers=cfg.REQUEST_HEADER)
        # print(
        #     f"/{cfg.layer_type}/{cfg.layer}/{cfg.projection}/{points[0]}/{points[1]}/{points[2]}{cfg.image_format}")
        # print(customer)

    host = cfg.HOST
