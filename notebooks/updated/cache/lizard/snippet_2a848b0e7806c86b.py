def get_anniversary_periods(start, finish, anniversary=1):
    import sys
    current = start
    periods = []
    while current <= finish:
        period_start, period_finish = date_period(DATE_FREQUENCY_MONTHLY,
            anniversary, current)
        current = period_start + relativedelta(months=+1)
        period_start = period_start if period_start > start else start
        period_finish = period_finish if period_finish < finish else finish
        periods.append((period_start, period_finish))
    return periods