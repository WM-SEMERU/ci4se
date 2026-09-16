def parse_equality(cls, equality_string):
    cls.register()
    assert '=' in equality_string, "There must be an '=' sign in the equality"
    [left_side, right_side] = equality_string.split('=', 1)
    left_side_value = yaml.safe_load(left_side.strip())
    right_side_value = yaml.safe_load(right_side.strip())
    assert isinstance(left_side_value, str
        ), 'Left side of equality must be a string'
    return left_side_value, right_side_value