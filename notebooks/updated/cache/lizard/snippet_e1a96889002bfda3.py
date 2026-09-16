def abort(self, exception=exc.ConnectError):
    log.warn('Aborting connection to %s:%s', self.host, self.port)

    def abort_pending(f):
        exc_info = sys.exc_info()
        if any(exc_info):
            f.set_exc_info(exc_info)
        else:
            f.set_exception(exception(self.host, self.port))
    for pending in self.drain_all_pending():
        abort_pending(pending)