def project_get(project_id=None, name=None, profile=None, **connection_args):
    auth(profile, **connection_args)
    if _OS_IDENTITY_API_VERSION > 2:
        return tenant_get(tenant_id=project_id, name=name, profile=None, **
            connection_args)
    else:
        return False