def _validate_field(param, fields):
    if param.field not in fields:
        raise InvalidQueryParams(**{'detail': 
            'The sort query param value of "%s" is invalid. That field does not exist on the resource being requested.'
             % param.raw_field, 'links': LINK, 'parameter': PARAM})