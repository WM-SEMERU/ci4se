def _dict_lookup_bitwise_add(cls, item, **kwargs):
    value_lookup = kwargs.get('value_lookup', False)
    test_zero = kwargs.get('test_zero', False)
    ret_val = None
    if str(item).lower() == 'not defined':
        return None
    if value_lookup:
        if not isinstance(item, list):
            return 'Invalid Value'
        ret_val = 0
    else:
        if not isinstance(item, six.integer_types):
            return 'Invalid Value'
        ret_val = []
    if 'lookup' in kwargs:
        for k, v in six.iteritems(kwargs['lookup']):
            if value_lookup:
                if six.text_type(v).lower() in [z.lower() for z in item]:
                    ret_val = ret_val + k
            else:
                do_test = True
                if not test_zero:
                    if k == 0:
                        do_test = False
                if do_test and isinstance(k, int) and item & k == k:
                    ret_val.append(v)
    else:
        return 'Invalid Value'
    return ret_val