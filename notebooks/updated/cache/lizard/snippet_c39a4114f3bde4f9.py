def disk_partitions(all=False):
    result = [dict(partition._asdict()) for partition in psutil.
        disk_partitions(all)]
    return result