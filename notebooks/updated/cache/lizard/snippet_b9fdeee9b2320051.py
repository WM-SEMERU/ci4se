def activate(locale, path=None):
    if path is None:
        path = _DEFAULT_LOCALE_PATH
    if locale not in _TRANSLATIONS:
        translation = gettext_module.translation('humanize', path, [locale])
        _TRANSLATIONS[locale] = translation
    _CURRENT.locale = locale
    return _TRANSLATIONS[locale]