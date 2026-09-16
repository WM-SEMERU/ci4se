def remove_quotes_around_tz(cls, timestr):
    quoted = cls.QUOTED_TIMEZONE.match(timestr)
    if quoted is not None:
        return quoted.group(1) + quoted.group(2)