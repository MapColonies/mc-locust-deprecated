from locust import HttpUser, between
from tasks.ApiTasks import ApiTasks
import os

class ApiUser(HttpUser):
    tasks = {
        ApiTasks: 1
    }
    wait_time = between(1, 5)
    
    host = os.getenv('TARGET_HOST', 'https://target-host.localhost')