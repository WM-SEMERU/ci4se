def _calculate_fake_duration():
    utc_start_time = datetime.datetime.utcnow()
    local_start_time = utc_start_time - (datetime.datetime.utcnow() -
        datetime.datetime.now())
    utc_finish_time = datetime.datetime.utcnow()
    start_time = local_start_time.time().isoformat()
    delta = utc_finish_time - utc_start_time
    duration = (delta.seconds * 1000000 + delta.microseconds) / 1000.0
    return start_time, duration