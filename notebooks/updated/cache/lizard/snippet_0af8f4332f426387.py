def makeB64UrlSafe(b64str):
    if isinstance(b64str, six.text_type):
        b64str = b64str.encode()
    return b64str.replace(b'+', b'-').replace(b'/', b'_')