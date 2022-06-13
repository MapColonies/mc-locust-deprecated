from test.get_ids import extract_ids, check_id
import time
from locust import HttpUser, task



class MyUserIdTask(HttpUser):
    wait_time = 1

    def __init__(self, *args, **kwargs):
        super().__init__(args, kwargs)
        self.response_id_data = None

    @task(1)
    def index(self):
        start = time.time()
        print("--- running Task")
        check_id(self.response_id_data)
        end = time.time()
        total = end - start


    def on_start(self):
        self.response_id_data = extract_ids()

