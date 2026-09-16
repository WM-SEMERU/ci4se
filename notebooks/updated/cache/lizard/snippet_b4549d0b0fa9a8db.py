def get_language_settings(language_code, site_id=None):
    from parler import appsettings
    return appsettings.PARLER_LANGUAGES.get_language(language_code, site_id)