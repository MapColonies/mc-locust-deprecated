import uuid
import json

from locust import TaskSet, task
from requests import Response

# from tools import GeneralTools


class ApiTasks(TaskSet):

    def on_start(self):
        """ on_start is called when a Locust start before any task is scheduled """
        pass

    def on_stop(self):
        """ on_stop is called when the TaskSet is stopping """
        pass

    @task(1)
    def FirstTest(self):
        print('First task..')