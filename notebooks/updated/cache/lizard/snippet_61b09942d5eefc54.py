def next_weekday(weekday):
    ix = WEEKDAYS.index(weekday)
    if ix == len(WEEKDAYS) - 1:
        return WEEKDAYS[0]
    return WEEKDAYS[ix + 1]