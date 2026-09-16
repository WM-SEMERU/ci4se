def from_string(locale, strict=True):
    language_code, country_code = Locale.decompose_locale(locale, strict)
    return Locale(language_code, country_code)