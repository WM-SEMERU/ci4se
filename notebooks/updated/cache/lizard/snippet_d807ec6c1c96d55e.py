def session_to_hour(timestamp):
    t = datetime.strptime(timestamp, SYNERGY_SESSION_PATTERN)
    return t.strftime(SYNERGY_HOURLY_PATTERN)