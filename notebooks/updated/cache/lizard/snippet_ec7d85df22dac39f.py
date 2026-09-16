def _get_status_timestamp(row):
    try:
        divs = row.find('div', {'id': 'coltextR3'}).find_all('div')
        if len(divs) < 2:
            return None
        timestamp_string = divs[1].string
    except AttributeError:
        return None
    try:
        return parse(timestamp_string)
    except ValueError:
        return None