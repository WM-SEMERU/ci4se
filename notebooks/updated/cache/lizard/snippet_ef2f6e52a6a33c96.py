def from_xx(cls, xx):
    xx = str(xx).lower()
    if xx is 'unknown':
        return UnknownLanguage(xx)
    try:
        return cls._from_xyz('ISO639', xx)
    except NotALanguageException:
        log.warning('Unknown ISO639: {}'.format(xx))
        return UnknownLanguage(xx)