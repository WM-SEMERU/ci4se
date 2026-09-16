def from_array(array):
    if array is None or not array:
        return None
    assert_type_or_raise(array, dict, parameter_name='array')
    data = {}
    data['latitude'] = float(array.get('latitude'))
    data['longitude'] = float(array.get('longitude'))
    data['live_period'] = int(array.get('live_period')) if array.get(
        'live_period') is not None else None
    instance = InputLocationMessageContent(**data)
    instance._raw = array
    return instance