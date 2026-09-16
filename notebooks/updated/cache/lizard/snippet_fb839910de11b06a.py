def from_json(cls, data):
    required_keys = 'solar_model', 'month', 'day_of_month'
    for key in required_keys:
        assert key in data, 'Required key "{}" is missing!'.format(key)
    if data['solar_model'] == 'ASHRAEClearSky':
        return OriginalClearSkyCondition.from_json(data)
    if data['solar_model'] == 'ASHRAETau':
        return RevisedClearSkyCondition.from_json(data)
    if 'daylight_savings_indicator' not in data:
        data['daylight_savings_indicator'] = 'No'
    optional_keys = 'beam_shced', 'diff_sched'
    for key in optional_keys:
        if key not in data:
            data[key] = ''
    return cls(data['month'], data['day_of_month'], data['clearness'], data
        ['daylight_savings_indicator'], data['beam_shced'], data['diff_sched'])