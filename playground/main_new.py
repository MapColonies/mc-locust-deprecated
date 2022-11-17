# import os
#
# from locust import between
# from locust import HttpUser
# from tasks.ApiTasks import ApiTasks
#
#
# class ApiUser(HttpUser):
#     tasks = {ApiTasks: 1}
#     wait_time = between(1, 5)
#
#     host = os.getenv("TARGET_HOST", "https://target-host.localhost")
# import itertools
# listOLists = [[5,6],[4,5,6],[7,8,9,10]]
# for l in itertools.product(*listOLists):
#     print(l)
import json

import glom

# def json_extract(obj, key):
#     """Recursively fetch values from nested JSON."""
#     arr = []
#
#     def extract(obj, arr, key):
#         """Recursively search for values of key in JSON tree."""
#         if isinstance(obj, dict):
#             for k, v in obj.items():
#                 if isinstance(v, (dict, list)):
#                     extract(v, arr, key)
#                 elif k == key:
#                     arr.append(v)
#         elif isinstance(obj, list):
#             for item in obj:
#                 extract(item, arr, key)
#         return arr
#
#     values = extract(obj, arr, key)
#     return values

with open("/home/shayavr/Downloads/shay_example.json", "r") as f:
    data_to_extract = json.load(f)
    print(data_to_extract)


urls = glom(data_to_extract, f)


#
# urls = json_extract(data_to_extract, 'request')
# print(urls[2])
