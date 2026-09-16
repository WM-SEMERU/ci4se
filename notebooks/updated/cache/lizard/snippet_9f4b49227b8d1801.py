def parse_uptime(uptime_str):
    years, weeks, days, hours, minutes = 0, 0, 0, 0, 0
    uptime_str = uptime_str.strip()
    time_list = uptime_str.split(',')
    for element in time_list:
        if re.search('year', element):
            years = int(element.split()[0])
        elif re.search('week', element):
            weeks = int(element.split()[0])
        elif re.search('day', element):
            days = int(element.split()[0])
        elif re.search('hour', element):
            hours = int(element.split()[0])
        elif re.search('minute', element):
            minutes = int(element.split()[0])
        elif re.search('second', element):
            seconds = int(element.split()[0])
    uptime_sec = (years * YEAR_SECONDS + weeks * WEEK_SECONDS + days *
        DAY_SECONDS + hours * 3600 + minutes * 60 + seconds)
    return uptime_sec