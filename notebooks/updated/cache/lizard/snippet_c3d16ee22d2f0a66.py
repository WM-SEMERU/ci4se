def generate_signature(secret, verb, url, nonce, data):
    parsedURL = urllib.parse.urlparse(url)
    path = parsedURL.path
    if parsedURL.query:
        path = path + '?' + parsedURL.query
    message = bytes(verb + path + str(nonce) + data, 'utf-8')
    signature = hmac.new(secret.encode('utf-8'), message, digestmod=hashlib
        .sha256).hexdigest()
    return signature