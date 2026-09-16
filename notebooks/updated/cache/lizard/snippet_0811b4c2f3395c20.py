def baseline(value):
    if value.value:
        _assert_is_type('shape.value', value.value, str_types)
        if value.value not in PropertySet._valid_baseline:
            raise ValueError(value.value + ' is not a valid baseline')