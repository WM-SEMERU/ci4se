def convert_time(self, time):
    time_string = str(datetime.timedelta(seconds=int(time)))
    if time_string.split(':')[0] == '0':
        time_string = time_string.partition(':')[2]
    return time_string