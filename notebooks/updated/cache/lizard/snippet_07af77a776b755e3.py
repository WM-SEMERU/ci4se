def check_password(self, username, password):
    try:
        if SUPPORTS_VERIFY:
            kerberos.checkPassword(username.lower(), password, getattr(
                settings, 'KRB5_SERVICE', ''), getattr(settings,
                'KRB5_REALM', ''), getattr(settings, 'KRB5_VERIFY_KDC', True))
        else:
            kerberos.checkPassword(username.lower(), password, getattr(
                settings, 'KRB5_SERVICE', ''), getattr(settings,
                'KRB5_REALM', ''))
        return True
    except kerberos.BasicAuthError:
        if getattr(settings, 'KRB5_DEBUG', False):
            logger.exception('Failure during authentication')
        return False
    except:
        if getattr(settings, 'KRB5_DEBUG', False):
            logger.exception('Failure during authentication')
        return False