def hourminsec(n_seconds):
    hours, remainder = divmod(n_seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    return abs(hours), abs(minutes), abs(seconds)