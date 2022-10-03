import os

from locust import between
from locust import HttpUser
from tasks.ApiTasks import ApiTasks


class ApiUser(HttpUser):
    tasks = {ApiTasks: 1}
    wait_time = between(1, 5)

    host = os.getenv("TARGET_HOST", "https://target-host.localhost")
