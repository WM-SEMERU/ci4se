def hold(name=None, pkgs=None, sources=None, **kwargs):
    if not name and not pkgs and not sources:
        raise SaltInvocationError(
            'One of name, pkgs, or sources must be specified.')
    if pkgs and sources:
        raise SaltInvocationError(
            'Only one of pkgs or sources can be specified.')
    targets = []
    if pkgs:
        targets.extend(pkgs)
    elif sources:
        for source in sources:
            targets.append(next(iter(source)))
    else:
        targets.append(name)
    ret = {}
    for target in targets:
        if isinstance(target, dict):
            target = next(iter(target))
        ret[target] = {'name': target, 'changes': {}, 'result': False,
            'comment': ''}
        state = _get_state(target)
        if not state:
            ret[target]['comment'] = 'Package {0} not currently held.'.format(
                target)
        elif state != 'hold':
            if 'test' in __opts__ and __opts__['test']:
                ret[target].update(result=None)
                ret[target]['comment'
                    ] = 'Package {0} is set to be held.'.format(target)
            else:
                result = _set_state(target, 'hold')
                ret[target].update(changes=result[target], result=True)
                ret[target]['comment'
                    ] = 'Package {0} is now being held.'.format(target)
        else:
            ret[target].update(result=True)
            ret[target]['comment'
                ] = 'Package {0} is already set to be held.'.format(target)
    return ret