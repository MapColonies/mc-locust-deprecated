from locust_plugins.csvreader import CSVReader
from locust import FastHttpUser, task
import common.config as conf



from common.config import path_builder

default_headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36',
    'X-API-KEY': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwicmVzb3VyY2VUeXBlcyI6WyJyYXN0ZXIiLCJkZW0iLCJ2ZWN0b3IiLCIzZCJdLCJpYXQiOjE1MTYyMzkwMjJ9.kidhXiB3ihor7FfkaduJxpJQXFMJGVH9fH7WI6GLGM0'}

URL_TO_ITERATE = path_builder
host_url = f"https://mapproxy-qa-mapproxy-route-raster.apps.v0h0bdx6.eastus.aroapp.io/"


class MyUser(FastHttpUser):
    @task
    def index(self):
        points = next(ssn_reader)
        self.client.get(
            f"{host_url}/{conf.layer_type}/{conf.layer}/{conf.projection}/{points[0]}/{points[1]}/{points[2]}{conf.image_format}",
            headers=default_headers)
        print(f"{host_url}/{conf.layer_type}/{conf.layer}/{conf.projection}/{points[0]}/{points[1]}/{points[2]}{conf.image_format}")
        # print(customer)

    host = f"https://mapproxy-qa-mapproxy-route-raster.apps.v0h0bdx6.eastus.aroapp.io/"


from locust import HttpUser, task, between
from tester.ew.op import choose_random_page
import os
import glob
from csv_data.manipulation import do_something
