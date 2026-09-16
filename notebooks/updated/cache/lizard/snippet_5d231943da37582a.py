def get_availabilities_for_duration(duration, availabilities):
    duration_availabilities = []
    start_time = '10:00'
    while start_time != '17:00':
        if start_time in availabilities:
            if duration == 30:
                duration_availabilities.append(start_time)
            elif increment_time_by_thirty_mins(start_time) in availabilities:
                duration_availabilities.append(start_time)
        start_time = increment_time_by_thirty_mins(start_time)
    return duration_availabilities