def cdn_url(request):
    cdn_url, ssl_url = _get_container_urls(CumulusStorage())
    static_url = settings.STATIC_URL
    return {'CDN_URL': cdn_url + static_url, 'CDN_SSL_URL': ssl_url +
        static_url}