def installed(name, version=None, defaults=False, force=False,
    preferred_state='stable'):
    if not isinstance(version, six.string_types) and version is not None:
        version = six.text_type(version)
    ret = {'name': name, 'result': None, 'comment': '', 'changes': {}}
    if '/' in name:
        channel, package = name.split('/')
    else:
        channel = None
        package = name
    installed_pecls = __salt__['pecl.list'](channel)
    if package in installed_pecls:
        if (version is None or version in installed_pecls[package]
            ) and preferred_state in installed_pecls[package]:
            ret['result'] = True
            ret['comment'] = 'Pecl extension {0} is already installed.'.format(
                name)
            return ret
    if version is not None:
        name = '{0}-{1}'.format(name, version)
    if __opts__['test']:
        ret['comment'] = 'Pecl extension {0} would have been installed'.format(
            name)
        return ret
    if __salt__['pecl.install'](name, defaults=defaults, force=force,
        preferred_state=preferred_state):
        ret['result'] = True
        ret['changes'][name] = 'Installed'
        ret['comment'
            ] = 'Pecl extension {0} was successfully installed'.format(name)
    else:
        ret['result'] = False
        ret['comment'] = 'Could not install pecl extension {0}.'.format(name)
    return ret