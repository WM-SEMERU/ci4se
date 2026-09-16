def read(message):
    require_compatible_version(message.physt_compatible)
    a_dict = _dict_from_v0342(message)
    return create_from_dict(a_dict, 'Message')