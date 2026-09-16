def hdfs_connect(host='localhost', port=50070, protocol='webhdfs',
    use_https='default', auth_mechanism='NOSASL', verify=True, session=None,
    **kwds):
    import requests
    if session is None:
        session = requests.Session()
    session.verify = verify
    if auth_mechanism in ('GSSAPI', 'LDAP'):
        if use_https == 'default':
            prefix = 'https'
        else:
            prefix = 'https' if use_https else 'http'
        try:
            import requests_kerberos
        except ImportError:
            raise IbisError(
                'Unable to import requests-kerberos, which is required for Kerberos HDFS support. Install it by executing `pip install requests-kerberos` or `pip install hdfs[kerberos]`.'
                )
        from hdfs.ext.kerberos import KerberosClient
        url = '{0}://{1}:{2}'.format(prefix, host, port)
        kwds.setdefault('mutual_auth', 'OPTIONAL')
        hdfs_client = KerberosClient(url, session=session, **kwds)
    else:
        if use_https == 'default':
            prefix = 'http'
        else:
            prefix = 'https' if use_https else 'http'
        from hdfs.client import InsecureClient
        url = '{}://{}:{}'.format(prefix, host, port)
        hdfs_client = InsecureClient(url, session=session, **kwds)
    return WebHDFS(hdfs_client)