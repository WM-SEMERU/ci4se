def field_timedelta_from_json(self, json_val):
    if isinstance(json_val, str):
        return timedelta(seconds=float(json_val))
    elif json_val is None:
        return None
    else:
        return timedelta(seconds=json_val)