def father(year=None):
    june_first = datetime.date(_year, 6, 1) if not year else datetime.date(int
        (year), 6, 1)
    weekday_seq = june_first.weekday()
    return datetime.date(june_first.year, 6, 21 - weekday_seq)