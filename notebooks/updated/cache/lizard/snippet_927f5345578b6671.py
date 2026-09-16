def _validate_handler(column_name, value, predicate_refs):
    if value is not None:
        for predicate_ref in predicate_refs:
            predicate, predicate_name, predicate_args = _decode_predicate_ref(
                predicate_ref)
            validate_result = predicate(value, *predicate_args)
            if isinstance(validate_result, dict
                ) and 'value' in validate_result:
                value = validate_result['value']
            elif type(validate_result) != bool:
                raise Exception(
                    'predicate (name={}) can only return bool or dict(value=new_value) value'
                    .format(predicate_name))
            elif not validate_result:
                raise ModelInvalid(
                    'db model validate failed: column={}, value={}, predicate={}, arguments={}'
                    .format(column_name, value, predicate_name, ','.join(
                    map(str, predicate_args))))
    return value