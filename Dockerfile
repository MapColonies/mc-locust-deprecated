# FROM python:3.6
#
# COPY docker-entrypoint.sh /
#
# RUN apt-get update -y && \
#   apt-get install build-essential -y && \
#   pip install --upgrade pip
#
# RUN  mkdir /locust
#
# COPY . /locust
#
# WORKDIR /locust
#
# RUN pip install -r requirements.txt
#
# EXPOSE 8089 5557 5558
#
# RUN useradd -ms /bin/bash user && usermod -a -G root user
#
# USER user
#
# # ENTRYPOINT ["/docker-entrypoint.sh"]
# RUN pip3 install flask
# RUN useradd -ms /bin/bash user && usermod -a -G root user

# USER user


# run mkdir /locust
# FROM locustio/locust
#
# COPY . /mnt/locust/
#
# WORKDIR /mnt/locust
#
# EXPOSE 8089

# ENTRYPOINT ["/mnt/locust/test-entrypoint.sh"]

# FROM python:3.6
#
#
# ENV VIRTUAL_ENV=/opt/venv
# RUN python3 -m venv $VIRTUAL_ENV
# ENV PATH=”$VIRTUAL_ENV/bin:$PATH”
#
# # RUN mkdir locust
#
# COPY . /locust
#
# WORKDIR /locust
#
# RUN pip install -r requirements.txt

# RUN mkdir locust
#
# COPY . /locust
#
# WORKDIR /locust


FROM locustio/locust
# RUN pip3 install pandas
# RUN pip3 install locust

# COPY . /mnt/locust/
# WORKDIR /mnt/locust/
WORKDIR /mnt/locust

COPY . .



