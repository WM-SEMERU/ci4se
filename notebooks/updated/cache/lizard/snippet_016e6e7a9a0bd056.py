def extend_validators(raw_validators, override_validators):
    if not raw_validators:
        return override_validators
    elif not override_validators:
        return raw_validators
    else:
        def_validators_mapping = _convert_validators_to_mapping(raw_validators)
        ref_validators_mapping = _convert_validators_to_mapping(
            override_validators)
        def_validators_mapping.update(ref_validators_mapping)
        return list(def_validators_mapping.values())