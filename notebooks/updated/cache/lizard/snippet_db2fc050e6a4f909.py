def frame_vars_to_xml(frame_f_locals, hidden_ns=None):
    xml = ''
    keys = dict_keys(frame_f_locals)
    if hasattr(keys, 'sort'):
        keys.sort()
    else:
        keys = sorted(keys)
    return_values_xml = ''
    for k in keys:
        try:
            v = frame_f_locals[k]
            eval_full_val = should_evaluate_full_value(v)
            if k == RETURN_VALUES_DICT:
                for name, val in dict_iter_items(v):
                    return_values_xml += var_to_xml(val, name,
                        additional_in_xml=' isRetVal="True"')
            elif hidden_ns is not None and k in hidden_ns:
                xml += var_to_xml(v, str(k), additional_in_xml=
                    ' isIPythonHidden="True"', evaluate_full_value=
                    eval_full_val)
            else:
                xml += var_to_xml(v, str(k), evaluate_full_value=eval_full_val)
        except Exception:
            pydev_log.exception('Unexpected error, recovered safely.')
    return return_values_xml + xml