def local_check(self):
    log.debug(LOG_CHECK, 'Checking %s', unicode(self))
    assert not self.extern[1], 'checking strict extern URL'
    log.debug(LOG_CHECK, 'checking connection')
    try:
        self.check_connection()
        self.set_content_type()
        self.add_size_info()
        self.aggregate.plugin_manager.run_connection_plugins(self)
    except tuple(ExcList) as exc:
        value = self.handle_exception()
        if isinstance(exc, socket.error) and exc.args[0] == -2:
            value = _('Hostname not found')
        elif isinstance(exc, UnicodeError):
            value = _('Bad hostname %(host)r: %(msg)s') % {'host': self.
                host, 'msg': str(value)}
        self.set_result(unicode_safe(value), valid=False)