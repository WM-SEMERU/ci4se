def _get_proxy_connection_details():
    proxytype = get_proxy_type()
    if proxytype == 'esxi':
        details = __salt__['esxi.get_details']()
    elif proxytype == 'esxcluster':
        details = __salt__['esxcluster.get_details']()
    elif proxytype == 'esxdatacenter':
        details = __salt__['esxdatacenter.get_details']()
    elif proxytype == 'vcenter':
        details = __salt__['vcenter.get_details']()
    elif proxytype == 'esxvm':
        details = __salt__['esxvm.get_details']()
    else:
        raise CommandExecutionError("'{0}' proxy is not supported".format(
            proxytype))
    return details.get('vcenter') if 'vcenter' in details else details.get(
        'host'), details.get('username'), details.get('password'), details.get(
        'protocol'), details.get('port'), details.get('mechanism'
        ), details.get('principal'), details.get('domain')