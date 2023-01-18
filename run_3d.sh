#!/bin/bash

docker run -it \
--net=host \
-e INPUT_PATH="CONF_FILE=/home/shayavr/Desktop/locust_configuration.json" \
-v /tmp/urls_data:/urls/csv_data \
extract-url-script:latest /bin/bash