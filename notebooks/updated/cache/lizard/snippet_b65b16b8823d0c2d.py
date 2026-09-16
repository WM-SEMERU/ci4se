def _InitSSLContext(self, cafile=None, disable_ssl_certificate_validation=False
    ):
    try:
        if disable_ssl_certificate_validation:
            ssl._create_default_https_context = ssl._create_unverified_context
            ssl_context = ssl.create_default_context()
        else:
            ssl_context = ssl.create_default_context(cafile=cafile)
    except AttributeError:
        return None
    return ssl_context