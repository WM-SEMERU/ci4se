def n_day(date_string):
    today = datetime.date.today()
    match = re.match('(\\d{1,3}|a) days? ago', date_string)
    groups = match.groups()
    if groups:
        decrement = groups[0]
        if decrement == 'a':
            decrement = 1
        return today - datetime.timedelta(days=int(decrement))
    return None