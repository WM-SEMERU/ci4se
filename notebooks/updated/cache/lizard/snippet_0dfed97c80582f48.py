def _collect_unrecognized_values(self, scheme, data, ancestors):
    if not isinstance(ancestors, OrderedDict):
        raise TypeError(
            'ancestors must be an OrderedDict. type: {0} was passed.'.
            format(type(ancestors)))
    if not isinstance(scheme, dict):
        raise TypeError('scheme must be a dict. type: {0} was passed'.
            format(type(scheme)))
    unrecognized_values = {}
    if isinstance(data, dict):
        pruned_scheme = [key for key in scheme.keys() if key not in
            RESERVED_SCHEME_KEYS and key[0] not in RESERVED_SCHEME_KEYS]
        for key, value in six.iteritems(data):
            if key in pruned_scheme:
                continue
            unrecognized_values[key] = value
        validations = scheme.get('is')
        if validations and 'one_of' in validations:
            for nested_scheme in validations['one_of']:
                if isinstance(nested_scheme, dict):
                    updated_scheme = self._update_scheme(nested_scheme,
                        ancestors)
                    pruned_scheme = [key for key in updated_scheme.keys() if
                        key not in RESERVED_SCHEME_KEYS and key[0] not in
                        RESERVED_SCHEME_KEYS]
                    for key in pruned_scheme:
                        if key in unrecognized_values:
                            del unrecognized_values[key]
    else:
        pass
    return unrecognized_values