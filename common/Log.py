import logging
import os
import time
from datetime import datetime

from pythonjsonlogger import jsonlogger


class CustomJsonFormatter(jsonlogger.JsonFormatter):
    def add_fields(self, log_record, record, message_dict):
        super(CustomJsonFormatter, self).add_fields(log_record, record, message_dict)
        if not log_record.get('timestamp'):
            # this doesn't use record.created, so it is slightly off
            now = datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%S.%fZ')
            log_record['timestamp'] = now
        if log_record.get('level'):
            log_record['level'] = log_record['level'].upper()
        else:
            log_record['level'] = record.levelname


LEVELS = {
    'debug': logging.DEBUG,
    'info': logging.INFO,
    'warning': logging.WARNING,
    'error': logging.ERROR,
    'critical': logging.CRITICAL
}

logger = logging.getLogger()
level = 'default'


def create_file(filename):
    path = filename[0:filename.rfind('/')]
    if not os.path.isdir(path):
        os.makedirs(path)
    if not os.path.isfile(filename):
        fd = open(filename, mode='w', encoding='utf-8')
        fd.close()
    else:
        pass


def set_file_handler(levels):
    if levels == 'error':
        logger.addHandler(MyLog.err_handler)
    logger.addHandler(MyLog.handler)


def set_stream_handler(levels, logs_format):
    if levels == 'error':
        handler = MyLog.stream_handler
        handler.setFormatter(CustomJsonFormatter(logs_format))
        logger.addHandler(MyLog.stream_handler)


def remove_handler(levels):
    if levels == 'error':
        logger.removeHandler(MyLog.err_handler)
    logger.removeHandler(MyLog.handler)


def get_current_time():
    return time.strftime(MyLog.date, time.localtime(time.time()))


class MyLog:
    path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    log_file = path + '/Log/log.log'
    err_file = path + '/Log/err.log'
    logger.setLevel(LEVELS.get(level, logging.NOTSET))
    create_file(log_file)
    create_file(err_file)
    date = '%Y-%m-%d %H:%M:%S'

    handler = logging.FileHandler(log_file, encoding='utf-8', mode='w')
    stream_handler = logging.StreamHandler()
    err_handler = logging.FileHandler(err_file, encoding='utf-8', mode='w')

    @staticmethod
    def debug(log_meg):
        set_file_handler('debug')
        logger.debug("[DEBUG " + get_current_time() + "]" + log_meg)
        remove_handler('debug')

    @staticmethod
    def info(log_meg):
        set_file_handler('info')
        logger.info("[INFO " + get_current_time() + "]" + log_meg)
        remove_handler('info')

    @staticmethod
    def warning(log_meg):
        set_file_handler('warning')
        logger.warning("[WARNING " + get_current_time() + "]" + log_meg)
        remove_handler('warning')

    @staticmethod
    def error(log_meg):
        set_file_handler('error')
        logger.error("[ERROR " + get_current_time() + "]" + log_meg)
        remove_handler('error')

    @staticmethod
    def critical(log_meg):
        set_file_handler('critical')
        logger.error("[CRITICAL " + get_current_time() + "]" + log_meg)
        remove_handler('critical')

    @staticmethod
    def stream_error(log_meg, log_fmt):
        set_stream_handler(levels='error', logs_format=log_fmt)
        logger.error(log_meg)
        remove_handler('error')

    @staticmethod
    def stream_debug(log_meg, log_fmt):
        set_stream_handler(levels='debug', logs_format=log_fmt)
        logger.debug(log_meg)
        remove_handler('debug')

    @staticmethod
    def stream_info(log_meg, log_fmt):
        set_stream_handler(levels='info', logs_format=log_fmt)
        logger.debug(log_meg)
        remove_handler('info')

    @staticmethod
    def stream_critical(log_meg, log_fmt):
        set_stream_handler(levels='critical', logs_format=log_fmt)
        logger.debug(log_meg)
        remove_handler('critical')

    @staticmethod
    def stream_warning(log_meg, log_fmt):
        set_stream_handler(levels='warning', logs_format=log_fmt)
        logger.debug(log_meg)
        remove_handler('warning')



