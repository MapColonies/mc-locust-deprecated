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
        wait_time = constant_pacing(cfg.WAIT_TIME)
        print("Choosing constant pacing wait time")
    else:
        print("Invalid wait function")

    @task(1)
    def index(self):
        points = next(ssn_reader)
        # print(cfg.TOKEN)

        with self.client.post(
            f"/{cfg.LAYER_TYPE}/{cfg.LAYER}/{cfg.GRIDNAME}/{points[0]}/{points[1]}/{points[2]}{cfg.IMAGE_FORMAT}?token={cfg.TOKEN}"
            # ,headers={"Authorization":"Bearer eyJhbGciOiJSUzI1NiIsImtpZCI6Ik1hcENvbG9uaWVzUUEifQ.eyJkIjpbInJhc3RlciIsInJhc3RlcldtcyIsInJhc3RlckV4cG9ydCIsImRlbSIsInZlY3RvciIsIjNkIl0sImlhdCI6MTY2Mzg2MzM0Mywic3ViIjoiTWFwQ29sb25pZXNRQSIsImlzcyI6Im1hcGNvbG9uaWVzLXRva2VuLWNsaSJ9.U_sx0Rsy96MA3xpIcWQHJ76xvK0PlHa--J1YILBYm2fCwtDdM4HLGagwq-OQQnBqi2e8KwktQ7sgt27hOJIPBHuONQS0ezBbuByk6UqN2S7P8WERdt8_lejuR1c94owQq7FOkhEaj_PKJ64ehXuMMHskfNeAIBf8GBN6QUGEenVx2w5k2rYBULoU30rpFkQVo8TtmiK2yGx0Ssx2k6LqSgCZfyZJbFzZ2MH3BPeCVleP1-zypaF9DS7SxS-EutL-gZ1e9bEccNktxQA4VMcjeTv45KYJLTIrccs_8gtPlzfaeNQFTIUKD-cRD1gyd_uLatPsl0wwHyFZIgRuJtcvfw?token=eyJhbGciOiJSUzI1NiIsImtpZCI6Ik1hcENvbG9uaWVzUUEifQ.eyJkIjpbInJhc3RlciIsInJhc3RlcldtcyIsInJhc3RlckV4cG9ydCIsImRlbSIsInZlY3RvciIsIjNkIl0sImlhdCI6MTY2Mzg2MzM0Mywic3ViIjoiTWFwQ29sb25pZXNRQSIsImlzcyI6Im1hcGNvbG9uaWVzLXRva2VuLWNsaSJ9.U_sx0Rsy96MA3xpIcWQHJ76xvK0PlHa--J1YILBYm2fCwtDdM4HLGagwq-OQQnBqi2e8KwktQ7sgt27hOJIPBHuONQS0ezBbuByk6UqN2S7P8WERdt8_lejuR1c94owQq7FOkhEaj_PKJ64ehXuMMHskfNeAIBf8GBN6QUGEenVx2w5k2rYBULoU30rpFkQVo8TtmiK2yGx0Ssx2k6LqSgCZfyZJbFzZ2MH3BPeCVleP1-zypaF9DS7SxS-EutL-gZ1e9bEccNktxQA4VMcjeTv45KYJLTIrccs_8gtPlzfaeNQFTIUKD-cRD1gyd_uLatPsl0wwHyFZIgRuJtcvfw"}
            # ,verify=False,
        ) as r:
            print(r.text)
    host = cfg.HOST
