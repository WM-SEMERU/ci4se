def _create_timezone_static(tz):
    timezone = icalendar.Timezone()
    timezone.add('TZID', tz)
    subcomp = icalendar.TimezoneStandard()
    subcomp.add('TZNAME', tz)
    subcomp.add('DTSTART', dt.datetime(1601, 1, 1))
    subcomp.add('RDATE', dt.datetime(1601, 1, 1))
    subcomp.add('TZOFFSETTO', tz._utcoffset)
    subcomp.add('TZOFFSETFROM', tz._utcoffset)
    timezone.add_component(subcomp)
    return timezone