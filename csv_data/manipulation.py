import logging
import os
import pandas as pd
from common import Log as logger
import itertools
from common.config import CSV_NAME

up_path = lambda _path, n: os.sep.join(_path.split(os.sep)[:-n])
URL_TO_ITERATE = 'https://mapproxy.com/{X_MAS}/{Y_MAS}/{Z_MAS}'
logging = logger.MyLog()


def do_something():
    logging.info(f"Reading csv {CSV_NAME} file")
    csv_path = os.path.join(os.path.dirname(__file__), "data", CSV_NAME)

    try:
        df = pd.read_csv(csv_path)
        logging.info(f'csv read from {csv_path}')
    except FileNotFoundError as err:
        logging.error("Failed to read csv , file not found")
        raise FileNotFoundError(f"{CSV_NAME} in path : {csv_path}")

    x_column = df['x'].tolist()
    y_column = df['y'].tolist()
    z_column = df['z'].tolist()

    logging.info("URL builder - looping on csv columns")

    url_list_to_run = []

    for (x, y, z) in zip(x_column, y_column, z_column):
        url_builder = URL_TO_ITERATE
        url_builder = url_builder.replace('{X_MAS}', str(x))
        url_builder = url_builder.replace('{Y_MAS}', str(y))
        url_builder = url_builder.replace('{Z_MAS}', str(z))
        url_list_to_run.append(url_builder)

    # print(df['x'].tolist())
    print("hello danny")
