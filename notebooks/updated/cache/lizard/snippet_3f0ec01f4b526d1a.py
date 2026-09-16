def virtualenv(self, virtualenv):
    if isinstance(virtualenv, bool):
        self._skip_virtualenv = virtualenv
    else:
        self._virtualenv = virtualenv
        if not os.path.isdir(self._virtualenv):
            raise Exception('virtualenv %s not found' % self._virtualenv)
        LOG.info('Using existing virtualenv at %s' % self._virtualenv)
        self._pkg_venv = self._virtualenv
        self._skip_virtualenv = True