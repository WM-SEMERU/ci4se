def timestamp(datetime_obj):
    start_of_time = datetime.datetime(1970, 1, 1)
    diff = datetime_obj - start_of_time
    return diff.total_seconds()