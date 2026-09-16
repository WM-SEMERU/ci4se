def py_to_couch_validate(key, val):
    if key not in RESULT_ARG_TYPES:
        raise CloudantArgumentError(116, key)
    if not isinstance(val, RESULT_ARG_TYPES[key]) or type(val
        ) is bool and int in RESULT_ARG_TYPES[key]:
        raise CloudantArgumentError(117, key, RESULT_ARG_TYPES[key])
    if key == 'keys':
        for key_list_val in val:
            if not isinstance(key_list_val, RESULT_ARG_TYPES['key']) or type(
                key_list_val) is bool:
                raise CloudantArgumentError(134, RESULT_ARG_TYPES['key'])
    if key == 'stale':
        if val not in ('ok', 'update_after'):
            raise CloudantArgumentError(135, val)