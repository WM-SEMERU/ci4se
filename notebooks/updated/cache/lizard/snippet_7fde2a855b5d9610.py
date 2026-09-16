def log(ltype, method, page, user_agent):
    try:
        f = open(settings.DJANGOSPAM_LOG, 'a')
        f.write('%s: %s method %s page %s user agent %s\n' % (datetime.
            datetime.now(), ltype, method, page, user_agent))
        f.close()
    except:
        if settings.DJANGOSPAM_FAIL_ON_LOG:
            exc_type, exc_value = sys.exc_info()[:2]
            raise LogError(exc_type, exc_value)