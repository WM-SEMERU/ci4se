def _kpost(url, data):
    headers = {'Content-Type': 'application/json'}
    log.trace('url is: %s, data is: %s', url, data)
    ret = http.query(url, method='POST', header_dict=headers, data=salt.
        utils.json.dumps(data))
    if ret.get('error'):
        return ret
    else:
        return salt.utils.json.loads(ret.get('body'))