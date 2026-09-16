def ordered_dict_to_dict(config):
    if type(config) == collections.OrderedDict:
        config = dict(config)
    if type(config) == list:
        for i in range(0, len(config)):
            config[i] = ordered_dict_to_dict(config[i])
    elif type(config) == dict:
        for key in config:
            config[key] = ordered_dict_to_dict(config[key])
    return config