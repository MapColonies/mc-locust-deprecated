import uuid
import json

from locust import TaskSet, task
from requests import Response

# from tools import GeneralTools

@events.init.add_listener
def _(environment, **_kwargs):
    print("2. Initializing locust, happens after parsing the locustfile but before test start")
    
@events.test_start.add_listener
def _(environment, **_kwargs):
    print("test listner")


class ApiTasks(TaskSet):

    def on_start(self):
        """ on_start is called when a Locust start before any task is scheduled """
        print("on start called")

    def on_stop(self):
        """ on_stop is called when the TaskSet is stopping """

        print("On Stoped called")

    @task(1)
    def FirstTest(self):
        # ssn_reader
        print('First task..')
