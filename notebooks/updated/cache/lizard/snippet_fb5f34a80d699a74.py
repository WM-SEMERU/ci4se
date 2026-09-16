def get_offset(target):
    from pytz import timezone
    import pytz
    from datetime import datetime
    utc = pytz.utc
    today = datetime.now()
    tz_target = timezone(tf.certain_timezone_at(lat=target['lat'], lng=
        target['lng']))
    today_target = tz_target.localize(today)
    today_utc = utc.localize(today)
    return (today_utc - today_target).total_seconds() / 60