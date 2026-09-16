def dateFormat(when):
    retval = ''
    if when is not None:
        dow = dateformat.format(when, 'l')
        dom = dateformat.format(when, 'jS')
        month = dateformat.format(when, 'F')
        if when.year != dt.date.today().year:
            retval = _('{weekday} {day} of {month} {year}').format(weekday=
                dow, day=dom, month=month, year=when.year)
        else:
            retval = _('{weekday} {day} of {month}').format(weekday=dow,
                day=dom, month=month)
    return retval