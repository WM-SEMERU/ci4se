def configman_keys(a_mapping):
    configmanized_keys_dict = DotDict()
    for k, v in iteritems_breadth_first(a_mapping):
        if '__' in k and k != k.upper():
            k = k.replace('__', '.')
        configmanized_keys_dict[k] = v
    return configmanized_keys_dict