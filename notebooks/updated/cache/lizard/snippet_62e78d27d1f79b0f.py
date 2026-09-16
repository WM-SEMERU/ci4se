def init_localization():
    locale.setlocale(locale.LC_ALL, '')
    loc = locale.getlocale()
    lang = loc[0][0:2] if loc[0] else 'en'
    filename = 'res/messages_%s.mo' % lang
    try:
        logging.debug('Opening message file %s for locale %s', filename, loc[0]
            )
        trans = gettext.GNUTranslations(open(filename, 'rb'))
    except IOError:
        logging.debug('Locale not found. Using default messages')
        trans = gettext.NullTranslations()
    trans.install()