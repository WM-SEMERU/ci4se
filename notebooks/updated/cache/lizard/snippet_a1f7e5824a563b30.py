def make_prefix(api_version, manipulator, auth_type):
    prefix = '%s_%s' % (api_version, manipulator)
    if auth_type and auth_type != 'none':
        prefix += '_' + auth_type
    return prefix