def get_simple_date(datestring):
    simple_date = re.compile('\\d{1,2}(\\.)\\d{1,2}')
    date = simple_date.search(datestring)
    if date:
        dates = date.group().split('.')
        if len(dates[0]) == 1:
            dates[0] = add_zero(dates[0])
        if len(dates[1]) == 1:
            dates[1] = add_zero(dates[1])
        if date_is_valid(dates):
            return '.'.join(dates) + '.'
        return 'Failed'