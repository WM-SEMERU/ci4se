def parse_time(s):
    result = None
    if 'epoch' in s:
        epoch_time = float(s.rstrip().split(' ')[1][:-1])
        result = datetime.datetime.utcfromtimestamp(epoch_time)
    else:
        _, date_part, time_part = s.split(' ')
        year, mon, day = date_part.split('/')
        hour, minute, sec = time_part.split(':')
        result = datetime.datetime(*map(int, (year, mon, day, hour, minute,
            sec)))
    return result