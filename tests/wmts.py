import logging

from locust import between
from locust import constant
from locust import constant_pacing
from locust import constant_throughput
from locust import HttpUser
from locust import task
from locust_plugins.csvreader import CSVReader

import common.config as cfg

ssn_reader = CSVReader("csv_data/data/new.csv")
# print(cfg.PRO_ACTIVE_WMTS_BBOX)
# x = MapproxyLayer(
#             layer_id="shay5",
#             zoom=0.0439453125,
#             product_bbox=[-180,-90,180,90],
#         )
# print(f"x_tile: {x.get_x_tile_ranges().range}")
# print(f"y_tile: {x.get_y_tile_ranges().range}")
# print(f"zoom: {x.get_zoom_range().range}")


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
        print(points)
        self.client.get(
            f"/{cfg.LAYER_TYPE}/{cfg.LAYER}/{cfg.GRIDNAME}/{points[0]}/{points[1]}/{points[2]}{cfg.IMAGE_FORMAT}?token={cfg.TOKEN}",
            # headers=cfg.REQUEST_HEADER,
        )

    host = cfg.HOST
