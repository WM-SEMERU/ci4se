def _parse_api_value_list(self, values):
    try:
        return [v.to_api() for v in values]
    except AttributeError:
        return list(values)