def package_removed(name, image=None, restart=False):
    ret = {'name': name, 'result': True, 'comment': '', 'changes': {}}
    if '~' not in name and not os.path.exists(name):
        if __opts__['test']:
            ret['result'] = None
        else:
            ret['result'] = False
        ret['comment'] = 'Package path {0} does not exist'.format(name)
        return ret
    old = __salt__['dism.installed_packages']()
    package_info = __salt__['dism.package_info'](name)
    if 'Package Identity' not in package_info or package_info[
        'Package Identity'] not in old:
        ret['comment'] = 'The package {0} is already removed'.format(name)
        return ret
    if __opts__['test']:
        ret['changes']['package'] = '{0} will be removed'.format(name)
        ret['result'] = None
        return ret
    status = __salt__['dism.remove_package'](name, image, restart)
    if status['retcode'] not in [0, 1641, 3010]:
        ret['comment'] = 'Failed to remove {0}: {1}'.format(name, status[
            'stdout'])
        ret['result'] = False
    new = __salt__['dism.installed_packages']()
    changes = salt.utils.data.compare_lists(old, new)
    if changes:
        ret['comment'] = 'Removed {0}'.format(name)
        ret['changes'] = status
        ret['changes']['package'] = changes
    return ret