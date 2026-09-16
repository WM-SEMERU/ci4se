def _filter_dates(dates, time_difference):
    LOGGER.debug('dates=%s', dates)
    if len(dates) <= 1:
        return dates
    sorted_dates = sorted(dates)
    separate_dates = [sorted_dates[0]]
    for curr_date in sorted_dates[1:]:
        if curr_date - separate_dates[-1] > time_difference:
            separate_dates.append(curr_date)
    return separate_dates