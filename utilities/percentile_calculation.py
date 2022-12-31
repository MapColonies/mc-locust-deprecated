import csv


def extract_response_time_from_record(csv_path: str):
    """
    This function return response time per request
    :param csv_path: path to the requests response time records
    :return:
    response_time_list: response time of requests
    """
    response_time_list = []
    with open(csv_path, 'r') as f:
        reader = csv.reader(f, delimiter=';')
        for row in reader:
            response_time_list.append(row[2])
    return response_time_list


def convert_to_millisecond(response_time_list: list):
    """
    This function gets a list of request response times in seconds
     and convert this list to a millisecond
    :param response_time_list: list of response time in seconds
    :return:
    rsp_millisecond: list of response time in millisecond
    """
    rsp_millisecond = []
    for rsp_time in response_time_list:
        rsp_millisecond.append(rsp_time * 1000)
    return rsp_millisecond


def count_rsp_time_by_rsp_time_ranges(rsp_time_data: list, rsp_range: tuple):
    rsp_counter = 0
    for rsp_time in rsp_time_data:
        if rsp_range[0] <= rsp_time <= rsp_range[1]:
            rsp_counter += 1
    return rsp_counter


def get_percentile_value(rsp_counter: float, rsp_time_list: list):
    """
    This function calculate the percentile value of the selected response time range of the total requests
    :param rsp_counter: The number of requests that was in the selected rsp range
    :param rsp_time_list:
    :return:
    percentile_value: percent value : float
    """
    percentile_value = rsp_counter / len(rsp_time_list) * 100
    return percentile_value
