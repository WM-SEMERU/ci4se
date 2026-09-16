def vserver_servicegroup_add(v_name, sg_name, **connection_args):
    ret = True
    if vserver_servicegroup_exists(v_name, sg_name, **connection_args):
        return False
    nitro = _connect(**connection_args)
    if nitro is None:
        return False
    vsg = NSLBVServerServiceGroupBinding()
    vsg.set_name(v_name)
    vsg.set_servicegroupname(sg_name)
    try:
        NSLBVServerServiceGroupBinding.add(nitro, vsg)
    except NSNitroError as error:
        log.debug(
            'netscaler module error - NSLBVServerServiceGroupBinding.add() failed: %s'
            , error)
        ret = False
    _disconnect(nitro)
    return ret