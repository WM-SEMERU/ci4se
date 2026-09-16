def _handle_status(self, key, value):
    if key in 'GOOD_PASSPHRASE':
        pass
    elif key == 'KEY_CONSIDERED':
        self.status = key.replace('_', ' ').lower()
    elif key == 'KEY_NOT_CREATED':
        self.status = 'key not created'
    elif key == 'KEY_CREATED':
        self.type, self.fingerprint = value.split()
        self.status = 'key created'
    elif key == 'NODATA':
        self.status = nodata(value)
    elif key == 'PROGRESS':
        self.status = progress(value.split(' ', 1)[0])
    elif key == 'PINENTRY_LAUNCHED':
        log.warn(
            """GnuPG has just attempted to launch whichever pinentry program you have configured, in order to obtain the passphrase for this key.  If you did not use the `passphrase=` parameter, please try doing so.  Otherwise, see Issues #122 and #137:
https://github.com/isislovecruft/python-gnupg/issues/122
https://github.com/isislovecruft/python-gnupg/issues/137"""
            )
        self.status = 'key not created'
    elif key.startswith('TRUST_') or key.startswith('PKA_TRUST_'
        ) or key == 'NEWSIG':
        pass
    else:
        raise ValueError('Unknown status message: %r' % key)
    if self.type in ('B', 'P'):
        self.primary_created = True
    if self.type in ('B', 'S'):
        self.subkey_created = True