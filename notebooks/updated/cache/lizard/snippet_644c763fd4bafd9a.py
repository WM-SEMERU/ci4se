def validate_cookies(session, class_name):
    if not do_we_have_enough_cookies(session.cookies, class_name):
        return False
    url = CLASS_URL.format(class_name=class_name) + '/class'
    r = session.head(url, allow_redirects=False)
    if r.status_code == 200:
        return True
    else:
        logging.debug('Stale session.')
        try:
            session.cookies.clear('.coursera.org')
        except KeyError:
            pass
        return False