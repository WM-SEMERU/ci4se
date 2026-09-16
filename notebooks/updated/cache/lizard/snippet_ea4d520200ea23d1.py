def by_range(self, chamber, start, end):
    check_chamber(chamber)
    start, end = parse_date(start), parse_date(end)
    if start > end:
        start, end = end, start
    path = '{chamber}/votes/{start:%Y-%m-%d}/{end:%Y-%m-%d}.json'.format(
        chamber=chamber, start=start, end=end)
    return self.fetch(path, parse=lambda r: r['results'])