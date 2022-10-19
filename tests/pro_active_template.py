import time
from datetime import date
from datetime import datetime
from random import shuffle
from typing import Iterable
from typing import Iterator

from locust import constant
from locust import events
from locust import HttpUser
from locust import task
from locust import TaskSet
from locust import User

from common.utils import WMTSIterator


# ssn_reader = [WMTSIterator(1, 5+1), WMTSIterator(5, 10), WMTSIterator(10, 15)]

# ssn_reader = WMTSIterator(range(0, 5))

lst = list(range(1, 11))
# shuffle(lst)
now = datetime.now()

# count = range(0,5)
# ssn_reader = iter(count)


@events.test_start.add_listener
def on_test_start(environment, **kwargs):
    current_time = now.strftime("%H:%M:%S")
    today = date.today()
    print(f"Test Started \nCurrent Time : {current_time} \nToday's date: {today} ")


@events.test_stop.add_listener
def on_test_stop(environment, **kwargs):
    current_time = now.strftime("%H:%M:%S")
    today = date.today()
    print(f"Test Ended \nCurrent Time : {current_time} \nToday's date: {today} ")


# class ProActiveUser(HttpUser):
#     wait_time = constant(60)

#     @task(1)
#     def index(self):
#         self.client.get('/')


class MyTaskSet(TaskSet):
    @task(1)
    def fast(self):
        self.client.get("/", name="fast_check")
        # points_1 = next(ssn_reader)
        shuffle(lst)
        print(lst[0])
        # points_2 = next(ssn_reader[1])
        # points_3 = next(ssn_reader[2])
        # print(f'{points_1} ,{points_2}, {points_3}')

        # print(next(iter_count))

    # @task(1)
    # def slow(self):
    #     # time.sleep(30)
    #     self.client.get("/", name="slow_check")


class MyLocust(HttpUser):
    wait_time = constant(30)
    tasks = [MyTaskSet]
