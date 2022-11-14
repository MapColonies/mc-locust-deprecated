from locust import HttpUser, task, between
from gevent.pool import Group

# getting below value from all tiles urls
num_of_parallel_requests = 25
class User(HttpUser):
    wait_time = between(0.05, 0.1)
    url = '/api/v1/test'
    @task(1)
    def test_api(self):
        group = Group()
        # This will spawn the number of requests needed in parallel
        for i in range(0, num_of_parallel_requests):

             group.spawn(lambda:self.client.get(url)))
        # Once they are ready they are hit in parallel
        group.join()