def project_list(profile=None, **connection_args):
    auth(profile, **connection_args)
    if _OS_IDENTITY_API_VERSION > 2:
        return tenant_list(profile, **connection_args)
    else:
        return False