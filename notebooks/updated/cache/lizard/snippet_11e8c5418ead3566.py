def absent(name, keys=None, user=None, gnupghome=None, **kwargs):
    ret = {'name': name, 'result': True, 'changes': {}, 'comment': []}
    _current_keys = __salt__['gpg.list_keys']()
    current_keys = []
    for key in _current_keys:
        current_keys.append(key['keyid'])
    if not keys:
        keys = name
    if isinstance(keys, six.string_types):
        keys = [keys]
    for key in keys:
        if key in current_keys:
            result = __salt__['gpg.delete_key'](key, user, gnupghome)
            if 'result' in result and not result['result']:
                ret['result'] = result['result']
                ret['comment'].append(result['comment'])
            else:
                ret['comment'].append('Deleting {0} from GPG keychain'.
                    format(name))
        else:
            ret['comment'].append('{0} not found in GPG keychain'.format(name))
    ret['comment'] = '\n'.join(ret['comment'])
    return ret