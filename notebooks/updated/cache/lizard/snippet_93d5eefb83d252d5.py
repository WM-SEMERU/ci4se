def validate_process_steps(prop, value):
    if value is not None:
        validate_type(prop, value, (dict, list))
        procstep_keys = set(_complex_definitions[prop])
        for idx, procstep in enumerate(wrap_value(value)):
            ps_idx = prop + '[' + str(idx) + ']'
            validate_type(ps_idx, procstep, dict)
            for ps_prop, ps_val in iteritems(procstep):
                ps_key = '.'.join((ps_idx, ps_prop))
                if ps_prop not in procstep_keys:
                    _validation_error(prop, None, value, 'keys: {0}'.format
                        (','.join(procstep_keys)))
                if ps_prop != 'sources':
                    validate_type(ps_key, ps_val, string_types)
                else:
                    validate_type(ps_key, ps_val, (string_types, list))
                    for src_idx, src_val in enumerate(wrap_value(ps_val)):
                        src_key = ps_key + '[' + str(src_idx) + ']'
                        validate_type(src_key, src_val, string_types)