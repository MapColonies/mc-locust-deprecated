# from csv_data.manipulation import do_something
from locust import HttpUser, task, between


class QuickstartUser(HttpUser):
    wait_time = between(1, 2.5)

    @task
    def hello_world(self):
        print("hello from task")
        # do_something()
#

