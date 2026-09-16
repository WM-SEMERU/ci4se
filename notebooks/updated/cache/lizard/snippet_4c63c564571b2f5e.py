def _proxy_settings(self):
    if not ('https_proxy' in environ or 'HTTPS_PROXY' in environ or 
        'http_proxy' in environ or 'HTTP_PROXY' in environ):
        return {}
    https_proxy = environ.get('https_proxy')
    if https_proxy is None:
        https_proxy = environ.get('HTTPS_PROXY')
    http_proxy = environ.get('http_proxy')
    if http_proxy is None:
        http_proxy = environ.get('HTTP_PROXY')
    no_proxy = environ.get('no_proxy')
    if no_proxy is None:
        no_proxy = environ.get('NO_PROXY', '')
    no_proxy = no_proxy + ',solr,db'
    out = [
        """PATH="/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games\"
"""
        ]
    if https_proxy is not None:
        out.append('https_proxy=' + posix_quote(https_proxy) + '\n')
        out.append('HTTPS_PROXY=' + posix_quote(https_proxy) + '\n')
    if http_proxy is not None:
        out.append('http_proxy=' + posix_quote(http_proxy) + '\n')
        out.append('HTTP_PROXY=' + posix_quote(http_proxy) + '\n')
    if no_proxy is not None:
        out.append('no_proxy=' + posix_quote(no_proxy) + '\n')
        out.append('NO_PROXY=' + posix_quote(no_proxy) + '\n')
    with open(self.sitedir + '/run/proxy-environment', 'w') as f:
        f.write(''.join(out))
    return {(self.sitedir + '/run/proxy-environment'): '/etc/environment'}