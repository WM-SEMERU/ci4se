def get_keystone_manager_from_identity_service_context():
    context = IdentityServiceContext()()
    if not context:
        msg = 'Identity service context cannot be generated'
        log(msg, level=ERROR)
        raise ValueError(msg)
    endpoint = format_endpoint(context['service_protocol'], context[
        'service_host'], context['service_port'], context['api_version'])
    if context['api_version'] in (2, '2.0'):
        api_version = 2
    else:
        api_version = 3
    return get_keystone_manager(endpoint, api_version, username=context[
        'admin_user'], password=context['admin_password'], tenant_name=
        context['admin_tenant_name'])