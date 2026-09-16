def detect_language_filename(cls, filename):
    log.debug('detect_language(filename="{}") ...'.format(filename))
    root, _ = os.path.splitext(filename)
    fn_lang = cls.DETECT_LANGUAGE_REGEX.findall(root)
    if fn_lang:
        language_part = fn_lang[0]
        try:
            lang = Language.from_unknown(language_part, xx=True, xxx=True)
            log.debug('... SUCCESS: detected from filename: {lang}'.format(
                lang=lang))
            return lang
        except NotALanguageException:
            pass
    else:
        log.debug('... FAIL: could not detect from filename')
    return UnknownLanguage.create_generic()