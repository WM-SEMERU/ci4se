def set_cookies():
    cookies = dict(request.args.items())
    r = app.make_response(redirect(url_for('view_cookies')))
    for key, value in cookies.items():
        r.set_cookie(key=key, value=value, secure=secure_cookie())
    return r