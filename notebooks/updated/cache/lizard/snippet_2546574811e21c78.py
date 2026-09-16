def _sign_url(self, base_url, params, security_key):
    import hashlib
    if six.PY3:
        from urllib.parse import urlencode, quote, quote_plus
    else:
        from urllib import urlencode, quote, quote_plus
    if not base_url or not self.security_key:
        return None
    params = params.copy()
    address = params.pop('address')
    url = base_url + '?address=' + address + '&' + urlencode(params)
    encoded_url = quote(url, safe="/:=&?#+!$,;'@()*[]")
    signature = quote_plus(encoded_url + self.security_key).encode('utf-8')
    encoded_signature = hashlib.md5(signature).hexdigest()
    return encoded_signature