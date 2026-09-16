def is_url_connectable(port):
    try:
        from urllib import request as url_request
    except ImportError:
        import urllib2 as url_request
    try:
        res = url_request.urlopen('http://127.0.0.1:%s/status' % port)
        if res.getcode() == 200:
            return True
        else:
            return False
    except Exception:
        return False