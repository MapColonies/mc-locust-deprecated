from locust import constant
from locust import tag
from locust import task
from locust import User


class MyUser(User):
    wait_time = constant(1)

    @tag("tag1")
    @task
    def task1(self):
        print("tag1")

    @tag("tag1", "tag2")
    @task
    def task2(self):
        print("tag1, tag2")

    @tag("tag3")
    @task
    def task3(self):
        print("tag3")

    @task
    def task4(self):
        print("task 4")
