def modify_cache_parameter_group(name, region=None, key=None, keyid=None,
    profile=None, **args):
    args = dict([(k, v) for k, v in args.items() if not k.startswith('_')])
    try:
        Params = args['ParameterNameValues']
    except ValueError as e:
        raise SaltInvocationError(
            'Invalid `ParameterNameValues` structure passed.')
    while Params:
        args.update({'ParameterNameValues': Params[:20]})
        Params = Params[20:]
        if not _modify_resource(name, name_param='CacheParameterGroupName',
            desc='cache parameter group', res_type='cache_parameter_group',
            region=region, key=key, keyid=keyid, profile=profile, **args):
            return False
    return True