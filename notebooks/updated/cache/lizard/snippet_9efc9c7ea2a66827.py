def get_localized_property(context, field=None, language=None):
    if language:
        return getattr(context, get_real_fieldname(field, language))
    if hasattr(settings, 'FALLBACK_LANGUAGES'):
        attrs = [translation.get_language()]
        attrs += get_fallback_languages()
    else:
        attrs = [translation.get_language(), translation.get_language()[:2],
            settings.LANGUAGE_CODE]

    def predicate(x):
        value = getattr(context, get_real_fieldname(field, x), None)
        return value if valid_for_gettext(value) else None
    return first_match(predicate, attrs)