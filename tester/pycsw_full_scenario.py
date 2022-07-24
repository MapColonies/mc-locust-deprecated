from locust import user, task, HttpUser

class SizingUser(HttpUser):
    # wait_time = constant(1)

    @task
    def get_records_by_polygon(self):
        self.client.get('/calendar')
        # print(type(ssn_reader))

    @task
    def get_records_by_id(self):
        pass
    
    @task
    def get_records_by_bbox(self):
        pass
    
    @task
    def get_records_by_country(self):
        pass