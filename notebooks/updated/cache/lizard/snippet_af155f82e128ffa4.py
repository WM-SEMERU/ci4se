def get_content(self, page, language, ctype, language_fallback=False):
    if page is None:
        page = fake_page
    if ' ' in ctype:
        raise ValueError('Ctype cannot contain spaces.')
    if not language:
        language = settings.PAGE_DEFAULT_LANGUAGE
    frozen = int(bool(page.freeze_date))
    key = self.PAGE_CONTENT_DICT_KEY % (page.id, ctype, frozen)
    key = key.replace(' ', '-')
    if page._content_dict is None:
        page._content_dict = dict()
    if page._content_dict.get(key, None):
        content_dict = page._content_dict.get(key)
    else:
        content_dict = cache.get(key)
    if not content_dict:
        content_dict = {}
        for lang in settings.PAGE_LANGUAGES:
            try:
                content = self.get_content_object(page, lang[0], ctype)
                content_dict[lang[0]] = content.body
            except self.model.DoesNotExist:
                content_dict[lang[0]] = ''
        page._content_dict[key] = content_dict
        cache.set(key, content_dict)
    if language in content_dict and content_dict[language]:
        return content_dict[language]
    if language_fallback:
        for lang in settings.PAGE_LANGUAGES:
            if lang[0] in content_dict and content_dict[lang[0]]:
                return content_dict[lang[0]]
    return ''