def remove_redirect(self, name):
    if not isinstance(name, basestring):
        raise TypeError('name can only be an instance of type basestring')
    self._call('removeRedirect', in_p=[name])