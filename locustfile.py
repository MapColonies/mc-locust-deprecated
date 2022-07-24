from locust import HttpUser, User, constant, task, tag 


class MyUser(HttpUser):
    wait_time = constant(1)

    @tag('tag1')
    @task
    def task1(self):
        self.client.get('GET', '/calendar')
