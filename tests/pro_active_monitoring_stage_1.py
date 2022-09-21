from asyncio import tasks
from locust import HttpUser, constant, User
from locust import events, task

from datetime import datetime
from datetime import date

from locust import TaskSet
import time
now = datetime.now()


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
        self.client.get("/",name="fast_check")

    @task(1)
    def slow(self):
        time.sleep(60)
        self.client.get("/",name="slow_check")

class MyLocust(HttpUser):
    wait_time = constant(60)
    tasks = [MyTaskSet]