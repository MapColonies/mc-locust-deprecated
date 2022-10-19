import glob
import os

from locust import between
from locust import FastHttpUser
from locust import HttpUser
from locust import task
from locust_plugins.csvreader import CSVReader

import common.config as conf
from common.config import path_builder
from csv_data.manipulation import do_something
from playground.temp_lib.op import choose_random_page

default_headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36"
}
URL_TO_ITERATE = path_builder
host_url = f"https://mapproxy-qa-mapproxy-route-raster.apps.v0h0bdx6.eastus.aroapp.io/"


class MyUser(FastHttpUser):
    @task
    # ToDo : Hello
    def index(self):
        points = next(ssn_reader)
        self.client.get(
            f"{host_url}/{conf.layer_type}/{conf.layer}/{conf.projection}/{points[0]}/{points[1]}/{points[2]}{conf.image_format}",
            headers=default_headers,
        )
        print(
            f"{host_url}/{conf.layer_type}/{conf.layer}/{conf.projection}/{points[0]}/{points[1]}/{points[2]}{conf.image_format}"
        )
        # print(customer)

    host = f"https://mapproxy-qa-mapproxy-route-raster.apps.v0h0bdx6.eastus.aroapp.io/"
