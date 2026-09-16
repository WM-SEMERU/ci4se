def version(*names, **kwargs):
    with_origin = kwargs.pop('with_origin', False)
    ret = __salt__['pkg_resource.version'](*names, **kwargs)
    if not salt.utils.data.is_true(with_origin):
        return ret
    if len(names) == 1:
        ret = {names[0]: ret}
    origins = __context__.get('pkg.origin', {})
    return dict([(x, {'origin': origins.get(x, ''), 'version': y}) for x, y in
        six.iteritems(ret)])