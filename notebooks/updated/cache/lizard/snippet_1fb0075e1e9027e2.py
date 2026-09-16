def from_json(cls, data):
    required_keys = ('location', 'direct_normal_irradiance',
        'diffuse_horizontal_irradiance')
    optional_keys = 'timestep', 'is_leap_year'
    for key in required_keys:
        assert key in data, 'Required key "{}" is missing!'.format(key)
    for key in optional_keys:
        if key not in data:
            data[key] = None
    location = Location.from_json(data['location'])
    direct_normal_irradiance = HourlyContinuousCollection.from_json(data[
        'direct_normal_irradiance'])
    diffuse_horizontal_irradiance = HourlyContinuousCollection.from_json(data
        ['diffuse_horizontal_irradiance'])
    timestep = data['timestep']
    is_leap_year = data['is_leap_year']
    return cls(location, direct_normal_irradiance,
        diffuse_horizontal_irradiance, timestep, is_leap_year)