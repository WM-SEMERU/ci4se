def b64_hmac_md5(key, data):
    bdigest = base64.b64encode(hmac.new(key, data, _md5).digest()).strip(
        ).decode('utf-8')
    return re.sub('=+$', '', bdigest)