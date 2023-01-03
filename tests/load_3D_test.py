#!/usr/bin/env python
import os
import sys

from utilities.percentile_calculation import write_rsp_time_percentile_ranges, get_percentile_value, \
    count_rsp_time_by_rsp_time_ranges, convert_to_millisecond, extract_response_time_from_record

myDir = os.getcwd()
sys.path.append(myDir)
from pathlib import Path

path = Path(myDir)
a = str(path.parent.absolute())
sys.path.append(a)

from locust import between, events
from locust import constant
from locust import constant_pacing
from locust import constant_throughput
from locust import HttpUser
from locust import task
from locust_plugins.csvreader import CSVReader
import common.config as cfg

# pvc_url = cfg.PVC_HANDLER_ROUTE
# response_param = requests.get(url=f'http://{pvc_url}{config.UPDATE_LAYER_DATA_DIR}/',
#                               params={'file': layers_name})
# ssn_reader = CSVReader(cfg.CSV_PATH_3D)

stat_file = open('stats.csv', 'w')
ssn_reader = CSVReader("/home/shayavr/Desktop/git/automation-locust/csv_data/urls_data.csv")


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

    @task(1)
    def index(self):
        url = next(ssn_reader)
        self.client.get(url=f"/{url[1]}", verify=False)

    def on_stop(self):
        rsp_list = extract_response_time_from_record(csv_path=f"{os.getcwd()}/stats.csv")
        print(rsp_list)
        rsp_list_millisecond = convert_to_millisecond(response_time_list=rsp_list)
        print(rsp_list_millisecond)
        percentile_rages_dict = {}
        rsp_time_ranges = [(0, 100), (101 - 500), (501, None)]
        for idx, rsp_t_range in rsp_time_ranges:
            counter = count_rsp_time_by_rsp_time_ranges(rsp_time_data=rsp_list_millisecond, rsp_range=rsp_t_range)
            print(counter)
            percentile = get_percentile_value(rsp_counter=counter, rsp_time_list=rsp_list_millisecond)
            percentile_rages_dict[str(rsp_time_ranges[idx])] = percentile
        write_rsp_time_percentile_ranges(percentile_rages_dict)
    #
    # host = cfg.HOST



# hook that is fired each time the request ends up with success
@events.request_success.add_listener
def hook_request_success(request_type, name, response_time, response_length, **kw):
    stat_file.write(request_type + ";" + name + ";" + str(response_time) + ";" + str(response_length) + "\n")


@events.quitting.add_listener
def hook_quitting(environment, **kw):
    stat_file.close()

