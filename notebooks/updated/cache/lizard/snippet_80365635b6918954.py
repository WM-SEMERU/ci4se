def set_cookie(response, name, value, expiry_seconds=None, secure=False):
    if expiry_seconds is None:
        expiry_seconds = 90 * 24 * 60 * 60
    expires = datetime.strftime(datetime.utcnow() + timedelta(seconds=
        expiry_seconds), '%a, %d-%b-%Y %H:%M:%S GMT')
    try:
        response.set_cookie(name, value, expires=expires, secure=secure)
    except (KeyError, TypeError):
        response.set_cookie(name.encode('utf-8'), value, expires=expires,
            secure=secure)