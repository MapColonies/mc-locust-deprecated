from prometheus_client import start_http_server, Summary , Counter
import random
import time

# Create a metric to track time spent and requests made.
REQUEST_TIME = Summary('request_processing_seconds', 'Time spent processing request')
c = Counter('danny', 'Description of counter')
# Decorate function with metric.
@REQUEST_TIME.time()
@c.count_exceptions()
def process_request(t):
    """A dummy function that takes some time."""
    time.sleep(t)
  
  
if __name__ == '__main__':
    # Start up the server to expose the metrics.
    start_http_server(8010)
    # Generate some requests.
    while True:
        c.inc()     # Increment by 1
       
        c.inc(1.6)  # Increment by given value
        process_request(random.random())