def hash_id(salt, user_id, requester, state):
    hash_type_to_format = {NAMEID_FORMAT_TRANSIENT: '{id}{req}{time}',
        NAMEID_FORMAT_PERSISTENT: '{id}{req}', 'pairwise': '{id}{req}',
        'public': '{id}', NAMEID_FORMAT_EMAILADDRESS: '{id}',
        NAMEID_FORMAT_UNSPECIFIED: '{id}'}
    format_args = {'id': user_id, 'req': requester, 'time': datetime.
        datetime.utcnow().timestamp()}
    hash_type = UserIdHasher.hash_type(state)
    try:
        fmt = hash_type_to_format[hash_type]
    except KeyError as e:
        raise ValueError('Unknown hash type: {}'.format(hash_type)) from e
    else:
        user_id = fmt.format(**format_args)
    hasher = (lambda salt, value: value) if hash_type in [
        NAMEID_FORMAT_EMAILADDRESS, NAMEID_FORMAT_UNSPECIFIED
        ] else util.hash_data
    return hasher(salt, user_id)