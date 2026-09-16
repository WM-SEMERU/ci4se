def install_locale(cls, locale_code, locale_type):
    if locale_code == getattr(cls, locale_type):
        return
    try:
        locale = Locale(locale_code)
        log.debug('Installed locale %s', locale_code)
    except UnknownLocaleError:
        default = settings.DEFAULT_LOCALIZATION_FORMAT
        log.warning('Unknown locale %s, falling back to %s', locale_code,
            default)
        locale = Locale(default)
    setattr(cls, locale_type, locale.language)