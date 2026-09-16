def ec2_credentials_create(user_id=None, name=None, tenant_id=None, tenant=
    None, profile=None, **connection_args):
    kstone = auth(profile, **connection_args)
    if name:
        user_id = user_get(name=name, profile=profile, **connection_args)[name
            ]['id']
    if not user_id:
        return {'Error': 'Could not resolve User ID'}
    if tenant:
        tenant_id = tenant_get(name=tenant, profile=profile, **connection_args
            )[tenant]['id']
    if not tenant_id:
        return {'Error': 'Could not resolve Tenant ID'}
    newec2 = kstone.ec2.create(user_id, tenant_id)
    return {'access': newec2.access, 'secret': newec2.secret, 'tenant_id':
        newec2.tenant_id, 'user_id': newec2.user_id}