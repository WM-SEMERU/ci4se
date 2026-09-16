def get_fallback_languages():
    lang = translation.get_language()
    fallback_list = settings.FALLBACK_LANGUAGES.get(lang, None)
    if fallback_list:
        return fallback_list
    return settings.FALLBACK_LANGUAGES.get(lang[:2], [])