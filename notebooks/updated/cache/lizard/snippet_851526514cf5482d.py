def _try_parse_basic_number(self, data):
    try:
        return int(data)
    except ValueError:
        pass
    try:
        return float(data)
    except ValueError:
        pass
    return data