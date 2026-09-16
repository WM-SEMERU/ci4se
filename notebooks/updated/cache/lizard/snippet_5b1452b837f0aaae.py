def check(self, **kwargs):
    errors = super().check(**kwargs)
    multitenant_staticfiles_dirs = settings.MULTITENANT_STATICFILES_DIRS
    if not isinstance(multitenant_staticfiles_dirs, (list, tuple)):
        errors.append(Error(
            'Your MULTITENANT_STATICFILES_DIRS setting is not a tuple or list.'
            , hint='Perhaps you forgot a trailing comma?'))
    return errors