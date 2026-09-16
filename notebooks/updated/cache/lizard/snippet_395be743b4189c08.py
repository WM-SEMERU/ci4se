def from_json(cls, data):
    required_keys = ('name', 'day_type', 'location', 'dry_bulb_condition',
        'humidity_condition', 'wind_condition', 'sky_condition')
    for key in required_keys:
        assert key in data, 'Required key "{}" is missing!'.format(key)
    return cls(data['name'], data['day_type'], Location.from_json(data[
        'location']), DryBulbCondition.from_json(data['dry_bulb_condition']
        ), HumidityCondition.from_json(data['humidity_condition']),
        WindCondition.from_json(data['wind_condition']), SkyCondition.
        from_json(data['sky_condition']))