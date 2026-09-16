def date_for_str(date_str):
    try:
        for date_format in itertools.permutations(['%Y', '%m', '%d']):
            try:
                date = datetime.strptime(date_str, ''.join(date_format))
                raise StopIteration
            except ValueError:
                pass
        return None
    except StopIteration:
        return date