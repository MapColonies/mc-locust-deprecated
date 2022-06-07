from locust import HttpUser , task
from locust_plugins.csvreader import CSVReader
import common.config as cfg
import time


print("hello")



ssn_reader = CSVReader("csv_data/data/wmts_csv_user.csv")
class MyUser(HttpUser):
    # wait_time = constant_throughput(1)
    @task(1)
    def index(self):
        start = time.time()
        for i in range(0, 5):
            points = next(ssn_reader)
            print(points)
        # points = next(ssn_reader)
        # print(points)
        # points = next(ssn_reader)
        # print(points)
        # points = next(ssn_reader)
        # print(points)
        # points = next(ssn_reader)
        # print(points)
        end = time.time()
        total = end - start
        print("One Task Finished {total}".format(total=total))
        # self.client.get(
        
        #     f"/wmts/2022_04_04T12_01_48Z_MAS_6_ORT_247557-Orthophoto/newGrids/1/0/1.png",
        #     headers=cfg.default_headers)
        # print(
        #     f"/wmts/2022_04_04T12_01_48Z_MAS_6_ORT_247557-Orthophoto/newGrids/1/0/1.png")
        # self.client.get(
        #     f"/{cfg.layer_type}/{cfg.layer}/{cfg.projection}/{points[0]}/{points[1]}/{points[2]}{cfg.image_format}",
        #     headers=cfg.REQUEST_HEADER)
        # print(
        #     f"/{cfg.layer_type}/{cfg.layer}/{cfg.projection}/{points[0]}/{points[1]}/{points[2]}{cfg.image_format}")
        # print(customer)

    host = cfg.HOST
