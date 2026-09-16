def active_translations(self, language_code=None, **translated_fields):
    language_codes = get_active_language_choices(language_code)
    return self.translated(*language_codes, **translated_fields)