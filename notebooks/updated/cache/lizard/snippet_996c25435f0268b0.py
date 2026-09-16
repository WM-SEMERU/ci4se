def validate_NUMPLACES(in_value, restriction):
    if type(restriction) is list:
        restriction = restriction[0]
    value = _get_val(in_value)
    if type(value) is list:
        for subval in value:
            if type(subval) is tuple:
                subval = subval[1]
            validate_NUMPLACES(subval, restriction)
    else:
        restriction = int(restriction)
        dec_val = Decimal(str(value))
        num_places = dec_val.as_tuple().exponent * -1
        if restriction != num_places:
            raise ValidationError('NUMPLACES: %s' % restriction)