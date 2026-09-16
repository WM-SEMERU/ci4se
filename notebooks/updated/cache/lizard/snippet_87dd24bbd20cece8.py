def get_tls_redis_url(redis_url):
    url = furl(redis_url)
    url.port += 1
    url.scheme += 's'
    url.args['ssl_cert_reqs'] = 'none'
    return str(url)