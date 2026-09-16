def _convert_validators_to_mapping(validators):
    validators_mapping = {}
    for validator in validators:
        if not isinstance(validator['check'], collections.Hashable):
            check = json.dumps(validator['check'])
        else:
            check = validator['check']
        key = check, validator['comparator']
        validators_mapping[key] = validator
    return validators_mapping