def slang_date(self, locale='en'):
    dt = pendulum.instance(self.datetime())
    try:
        return _translate(dt, locale)
    except KeyError:
        pass
    delta = humanize.time.abs_timedelta(timedelta(seconds=self.epoch - now(
        ).epoch))
    format_string = 'DD MMM'
    if delta.days >= 365:
        format_string += ' YYYY'
    return dt.format(format_string, locale=locale).title()