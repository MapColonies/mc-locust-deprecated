#!/usr/bin/env python
from locust import HttpUser, TaskSet, task, events, constant_pacing, between, constant_throughput, constant, tag
from locust.runners import MasterRunner

from locust_plugins.csvreader import CSVReader
import os
import sys

myDir = os.getcwd()
sys.path.append(myDir)
from pathlib import Path

path = Path(myDir)
a = str(path.parent.absolute())
sys.path.append(a)
from utilities.percentile_calculation import extract_response_time_from_record, \
    count_rsp_time_by_rsp_time_ranges, get_percentile_value, write_rsp_time_percentile_ranges

import requests
from locust import between
from locust import constant
from locust import constant_pacing
from locust import constant_throughput
from locust import HttpUser
from locust import task
from locust_plugins.csvreader import CSVReader
import common.config as cfg
from datetime import datetime

current_time = datetime.now()
current_time = current_time.strftime("%Y-%m-%d %H:%M:%S")




ssn_reader = CSVReader(cfg.CSV_PATH_3D)
requests_records_path = f"{cfg.ROOT_DIR}/csv_data/{current_time}.csv"
stat_file = open(requests_records_path, 'w')


class UserBehavior(TaskSet):
    """ Defines user behaviour in traffic simulation """

    @task(1)
    def index(self):
        url = next(ssn_reader)
        self.client.get(f"{url[1]}", verify=False)
        # self.client.get(url=url[1], verify=False)


class WebsiteUser(HttpUser):
    """ Defines user that will be used in traffic simulation """
    tasks = {UserBehavior: 2}
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

    def on_stop(self):
        rsp_list = extract_response_time_from_record(
            csv_path=requests_records_path)
        print(rsp_list)
        percentile_rages_dict = {}
        rsp_time_ranges = cfg.PERCENTILE_RANGES
        for idx, rsp_t_range in enumerate(rsp_time_ranges):
            counter = count_rsp_time_by_rsp_time_ranges(rsp_time_data=rsp_list, rsp_range=rsp_t_range)

            percentile = get_percentile_value(rsp_counter=counter, rsp_time_list=rsp_list)
            percentile_rages_dict[str(rsp_time_ranges[idx])] = percentile
        write_rsp_time_percentile_ranges(percentile_rages_dict)


# hook that is fired each time the request ends up with success
@events.request.add_listener
def hook_request_success(request_type, name, response_time, response_length, response, **kw):
    stat_file.write(
        str(response) + ";" + request_type + ";" + name + ";" + str(response_time) + ";" + str(response_length) + "\n")


@events.quitting.add_listener
def hook_quitting(environment, **kw):
    stat_file.close()
