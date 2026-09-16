def touch(filename, timestamp):
    if timestamp is not None:
        timestamp = timestamp, timestamp
    from os import utime
    utime(filename, timestamp)