from datetime import datetime

import pytz


ISO_8601_FORMAT = '%Y-%m-%dT%H:%M:%S.%fZ'


def str_to_datetime(string):
    return datetime.strptime(string, ISO_8601_FORMAT)


def datetime_to_str(dt):
    return dt.strftime(ISO_8601_FORMAT)
