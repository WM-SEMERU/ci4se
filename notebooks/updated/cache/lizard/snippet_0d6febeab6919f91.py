def day_to_month(timeperiod):
    t = datetime.strptime(timeperiod, SYNERGY_DAILY_PATTERN)
    return t.strftime(SYNERGY_MONTHLY_PATTERN)