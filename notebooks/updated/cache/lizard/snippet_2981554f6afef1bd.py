def toLocalTime(seconds, microseconds=0):
    delta = datetime.timedelta(seconds=seconds, microseconds=microseconds)
    return GPS_Epoch + delta