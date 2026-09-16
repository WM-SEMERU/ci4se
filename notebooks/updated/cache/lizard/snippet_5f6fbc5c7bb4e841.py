def get_rsa_props(object_class, exported_cfgs, remote_intents=None,
    ep_svc_id=None, fw_id=None, pkg_vers=None, service_intents=None):
    results = {}
    if not object_class:
        raise ArgumentError('object_class',
            'object_class must be an [] of Strings')
    results['objectClass'] = object_class
    if not exported_cfgs:
        raise ArgumentError('exported_cfgs',
            'exported_cfgs must be an array of Strings')
    results[REMOTE_CONFIGS_SUPPORTED] = exported_cfgs
    results[SERVICE_IMPORTED_CONFIGS] = exported_cfgs
    if remote_intents:
        results[REMOTE_INTENTS_SUPPORTED] = remote_intents
    if service_intents:
        results[SERVICE_INTENTS] = service_intents
    if not ep_svc_id:
        ep_svc_id = get_next_rsid()
    results[ENDPOINT_SERVICE_ID] = ep_svc_id
    results[SERVICE_ID] = ep_svc_id
    if not fw_id:
        fw_id = 'endpoint-in-error'
    results[ENDPOINT_FRAMEWORK_UUID] = fw_id
    if pkg_vers:
        if isinstance(pkg_vers, type(tuple())):
            pkg_vers = [pkg_vers]
        for pkg_ver in pkg_vers:
            results[pkg_ver[0]] = pkg_ver[1]
    results[ENDPOINT_ID] = create_uuid()
    results[SERVICE_IMPORTED] = 'true'
    return results