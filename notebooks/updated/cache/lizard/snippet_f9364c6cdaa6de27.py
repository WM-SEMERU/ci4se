def create_requests_session(retries=None, backoff_factor=None,
    status_forcelist=None, pools_size=4, maxsize=4, ssl_verify=None,
    ssl_cert=None, proxy=None, session=None):
    config = Configuration()
    if retries is None:
        if config.error_retry_max is None:
            retries = 5
        else:
            retries = config.error_retry_max
    if backoff_factor is None:
        if config.error_retry_backoff is None:
            backoff_factor = 0.23
        else:
            backoff_factor = config.error_retry_backoff
    if status_forcelist is None:
        if config.error_retry_codes is None:
            status_forcelist = [500, 502, 503, 504]
        else:
            status_forcelist = config.error_retry_codes
    if ssl_verify is None:
        ssl_verify = config.verify_ssl
    if ssl_cert is None:
        if config.cert_file and config.key_file:
            ssl_cert = config.cert_file, config.key_file
        elif config.cert_file:
            ssl_cert = config.cert_file
    if proxy is None:
        proxy = Configuration().proxy
    session = session or requests.Session()
    session.verify = ssl_verify
    session.cert = ssl_cert
    if proxy:
        session.proxies = {'http': proxy, 'https': proxy}
    retry = Retry(backoff_factor=backoff_factor, connect=retries,
        method_whitelist=False, read=retries, status_forcelist=tuple(
        status_forcelist), total=retries)
    adapter = HTTPAdapter(max_retries=retry, pool_connections=pools_size,
        pool_maxsize=maxsize, pool_block=True)
    session.mount('http://', adapter)
    session.mount('https://', adapter)
    return session