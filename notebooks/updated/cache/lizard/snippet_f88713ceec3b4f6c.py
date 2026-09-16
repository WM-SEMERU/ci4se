def iso_day_to_weekday(d):
    if int(d) == utils.get_now().isoweekday():
        return _('today')
    for w in WEEKDAYS:
        if w[0] == int(d):
            return w[1]