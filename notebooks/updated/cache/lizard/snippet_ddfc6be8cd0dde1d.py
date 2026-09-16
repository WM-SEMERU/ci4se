def GSSAuth(auth_method, gss_deleg_creds=True):
    if _API == 'MIT':
        return _SSH_GSSAPI(auth_method, gss_deleg_creds)
    elif _API == 'SSPI' and os.name == 'nt':
        return _SSH_SSPI(auth_method, gss_deleg_creds)
    else:
        raise ImportError('Unable to import a GSS-API / SSPI module!')