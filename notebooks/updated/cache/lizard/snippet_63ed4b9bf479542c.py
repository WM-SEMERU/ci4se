def SmartStubAdapter(host='localhost', port=443, path='/sdk', url=None,
    sock=None, poolSize=5, certFile=None, certKeyFile=None, httpProxyHost=
    None, httpProxyPort=80, sslProxyPath=None, thumbprint=None, cacertsFile
    =None, preferredApiVersions=None, acceptCompressedResponses=True,
    connectionPoolTimeout=CONNECTION_POOL_IDLE_TIMEOUT_SEC, samlToken=None,
    sslContext=None):
    if preferredApiVersions is None:
        preferredApiVersions = GetServiceVersions('vim25')
    sslContext = localSslFixup(host, sslContext)
    supportedVersion = __FindSupportedVersion('https' if port > 0 else
        'http', host, port, path, preferredApiVersions, sslContext)
    if supportedVersion is None:
        raise Exception('%s:%s is not a VIM server' % (host, port))
    return SoapStubAdapter(host=host, port=port, path=path, url=url, sock=
        sock, poolSize=poolSize, certFile=certFile, certKeyFile=certKeyFile,
        httpProxyHost=httpProxyHost, httpProxyPort=httpProxyPort,
        sslProxyPath=sslProxyPath, thumbprint=thumbprint, cacertsFile=
        cacertsFile, version=supportedVersion, acceptCompressedResponses=
        acceptCompressedResponses, connectionPoolTimeout=
        connectionPoolTimeout, samlToken=samlToken, sslContext=sslContext)