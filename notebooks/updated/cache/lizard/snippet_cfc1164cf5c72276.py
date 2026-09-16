def timer(diff, processed):
    minutes, seconds = divmod(diff, 60)
    try:
        time_per_request = diff / float(len(processed))
    except ZeroDivisionError:
        time_per_request = 0
    return minutes, seconds, time_per_request