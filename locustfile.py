from locust import constant
from locust import HttpUser
from locust import tag
from locust import task
from locust import User


class MyUser(HttpUser):
    wait_time = constant(1)

    @tag("tag1")
    @task
    def task1(self):
        self.client.get("GET", "/calendar")
