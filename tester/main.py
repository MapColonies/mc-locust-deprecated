from locust import HttpUser, task, between
from tester.ew.op import choose_random_page
import common.config as cfg
import os
import glob
from csv_data.manipulation import do_something
from locust_plugins.csvreader import CSVReader

runner_url_list = do_something()
ssn_reader = CSVReader("csv_data/data/wmts_csv_user.csv")


class MyUser(HttpUser):
    @task
    def index(self):
        points = next(ssn_reader)
        self.client.get(
            f"/wmts/2022_04_04T12_01_48Z_MAS_6_ORT_247557-Orthophoto/newGrids/1/0/1.png",
            headers=cfg.default_headers)
        print(
            f"/wmts/2022_04_04T12_01_48Z_MAS_6_ORT_247557-Orthophoto/newGrids/1/0/1.png")
        # self.client.get(
        #     f"/{cfg.layer_type}/{cfg.layer}/{cfg.projection}/{points[0]}/{points[1]}/{points[2]}{cfg.image_format}",
        #     headers=cfg.default_headers)
        # print(
        #     f"/{cfg.layer_type}/{cfg.layer}/{cfg.projection}/{points[0]}/{points[1]}/{points[2]}{cfg.image_format}")
        # print(customer)

    host = cfg.host
