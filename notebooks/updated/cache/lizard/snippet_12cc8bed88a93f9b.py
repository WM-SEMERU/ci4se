def sanitize_proxies(self):
    if os.name != 'posix':
        return
    if 'http' not in self['proxy']:
        http_proxy = get_gconf_http_proxy() or get_kde_http_proxy()
        if http_proxy:
            self['proxy']['http'] = http_proxy
    if 'ftp' not in self['proxy']:
        ftp_proxy = get_gconf_ftp_proxy() or get_kde_ftp_proxy()
        if ftp_proxy:
            self['proxy']['ftp'] = ftp_proxy