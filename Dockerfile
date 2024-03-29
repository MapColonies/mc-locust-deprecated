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


FROM locustio/locust:2.10.0


RUN pip install --upgrade pip



RUN pip install --upgrade setuptools_scm wheel virtualenv


RUN pip install pandas
RUN pip install locust_plugins
RUN pip install xmltodict
RUN pip install --upgrade setuptools
RUN pip install mc-automation-tools
# RUN pip3 install locust

# COPY . /mnt/locust/
# WORKDIR /mnt/locust/
WORKDIR /mnt/locust

COPY . /mnt/locust/


#RUN . /source_code/venv/bin/activate

# EXPOSE 8089 5557 5558
# ENTRYPOINT ["/docker-entrypoint.sh"]

# EXPOSE 8089
