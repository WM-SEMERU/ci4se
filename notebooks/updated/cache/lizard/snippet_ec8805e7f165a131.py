def modify_log_flags(self, settings):
    if not isinstance(settings, basestring):
        raise TypeError('settings can only be an instance of type basestring')
    self._call('modifyLogFlags', in_p=[settings])