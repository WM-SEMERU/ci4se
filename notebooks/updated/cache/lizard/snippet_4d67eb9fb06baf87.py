def connect(host='localhost', port=21050, database=None, timeout=None,
    use_ssl=False, ca_cert=None, auth_mechanism='NOSASL', user=None,
    password=None, kerberos_service_name='impala', use_ldap=None, ldap_user
    =None, ldap_password=None, use_kerberos=None, protocol=None, krb_host=None
    ):
    if use_kerberos is not None:
        warn_deprecate('use_kerberos', 'auth_mechanism="GSSAPI"')
        if use_kerberos:
            auth_mechanism = 'GSSAPI'
    if use_ldap is not None:
        warn_deprecate('use_ldap', 'auth_mechanism="LDAP"')
        if use_ldap:
            auth_mechanism = 'LDAP'
    if auth_mechanism:
        auth_mechanism = auth_mechanism.upper()
    else:
        auth_mechanism = 'NOSASL'
    if auth_mechanism not in AUTH_MECHANISMS:
        raise NotSupportedError('Unsupported authentication mechanism: {0}'
            .format(auth_mechanism))
    if ldap_user is not None:
        warn_deprecate('ldap_user', 'user')
        user = ldap_user
    if ldap_password is not None:
        warn_deprecate('ldap_password', 'password')
        password = ldap_password
    if protocol is not None:
        if protocol.lower() == 'hiveserver2':
            warn_protocol_param()
        else:
            raise NotSupportedError(
                "'{0}' is not a supported protocol; only HiveServer2 is supported"
                .format(protocol))
    service = hs2.connect(host=host, port=port, timeout=timeout, use_ssl=
        use_ssl, ca_cert=ca_cert, user=user, password=password,
        kerberos_service_name=kerberos_service_name, auth_mechanism=
        auth_mechanism, krb_host=krb_host)
    return hs2.HiveServer2Connection(service, default_db=database)