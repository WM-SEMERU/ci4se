def removed(name, ruby=None, user=None, gem_bin=None):
    ret = {'name': name, 'result': None, 'comment': '', 'changes': {}}
    if name not in __salt__['gem.list'](name, ruby, gem_bin=gem_bin, runas=user
        ):
        ret['result'] = True
        ret['comment'] = 'Gem is not installed.'
        return ret
    if __opts__['test']:
        ret['comment'] = 'The gem {0} would have been removed'.format(name)
        return ret
    if __salt__['gem.uninstall'](name, ruby, gem_bin=gem_bin, runas=user):
        ret['result'] = True
        ret['changes'][name] = 'Removed'
        ret['comment'] = 'Gem was successfully removed.'
    else:
        ret['result'] = False
        ret['comment'] = 'Could not remove gem.'
    return ret