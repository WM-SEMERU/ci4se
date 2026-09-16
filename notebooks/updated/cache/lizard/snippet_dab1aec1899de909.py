def _user_settings(self):
    user_settings = getattr(settings, self._name, {})
    if not user_settings and self._required:
        raise ImproperlyConfigured(
            'Settings file is missing dict options with name {}'.format(
            self._name))
    keys = frozenset(user_settings.keys())
    required = self._required - keys
    if required:
        raise ImproperlyConfigured(
            'Following options for {} are missing from settings file: {}'.
            format(self._name, ', '.join(sorted(required))))
    removed = keys & self._removed
    if removed:
        raise ImproperlyConfigured(
            'Following options for {} have been removed: {}'.format(self.
            _name, ', '.join(sorted(removed))))
    return user_settings