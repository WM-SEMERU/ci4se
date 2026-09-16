def validate_week(year, week):
    max_week = datetime.strptime('{}-{}-{}'.format(12, 31, year), '%m-%d-%Y'
        ).isocalendar()[1]
    if max_week == 1:
        max_week = 53
    return 1 <= week <= max_week