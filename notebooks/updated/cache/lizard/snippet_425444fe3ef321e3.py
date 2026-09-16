def _add_months(p_sourcedate, p_months):
    month = p_sourcedate.month - 1 + p_months
    year = p_sourcedate.year + month // 12
    month = month % 12 + 1
    day = min(p_sourcedate.day, calendar.monthrange(year, month)[1])
    return date(year, month, day)