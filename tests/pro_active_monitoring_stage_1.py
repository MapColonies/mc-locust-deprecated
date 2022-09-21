from asyncio import tasks
from typing import Iterable, Iterator
from locust import HttpUser, constant, User
from locust import events, task
import sys
from datetime import datetime
from datetime import date
from common.utils import WMTSIterator
from locust import TaskSet
import time


ssn_reader = [WMTSIterator(1, 5+1), WMTSIterator(5, 10), WMTSIterator(10, 15)]


now = datetime.now()

# count = range(0,5)
# ssn_reader = iter(count)


@events.test_start.add_listener
def on_test_start(environment, **kwargs):
    current_time = now.strftime("%H:%M:%S")
    today = date.today()
    print(
        f"Test Started \nCurrent Time : {current_time} \nToday's date: {today} ")


@events.test_stop.add_listener
def on_test_stop(environment, **kwargs):
    current_time = now.strftime("%H:%M:%S")
    today = date.today()
    print(
        f"Test Ended \nCurrent Time : {current_time} \nToday's date: {today} ")


# class ProActiveUser(HttpUser):
#     wait_time = constant(60)

#     @task(1)
#     def index(self):
#         self.client.get('/')

class MyTaskSet(TaskSet):
    @task(1)
    def fast(self):
        self.client.get("/", name="fast_check")
        points_1 = next(ssn_reader[0])
        points_2 = next(ssn_reader[1])
        points_3 = next(ssn_reader[2])
        print(f'{points_1} ,{points_2}, {points_3}')

        # print(next(iter_count))

    # @task(1)
    # def slow(self):
    #     # time.sleep(30)
    #     self.client.get("/", name="slow_check")


class MyLocust(HttpUser):
    wait_time = constant(2)
    tasks = [MyTaskSet]
