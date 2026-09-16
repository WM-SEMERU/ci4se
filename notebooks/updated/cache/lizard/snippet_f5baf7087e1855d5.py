def translator(self):
    if self._translator is None:
        languages = self.lang
        if not languages:
            return gettext.NullTranslations()
        if not isinstance(languages, list):
            languages = [languages]
        translator = gettext.NullTranslations()
        for name, i18n_dir in [('biryani', os.path.join(pkg_resources.
            get_distribution('biryani').location, 'biryani', 'i18n')), (
            conf['country_package'].replace('_', '-'), os.path.join(
            pkg_resources.get_distribution(conf['country_package']).
            location, conf['country_package'], 'i18n'))]:
            if i18n_dir is not None:
                translator = new_translator(name, i18n_dir, languages,
                    fallback=translator)
        translator = new_translator(conf['package_name'], conf['i18n_dir'],
            languages, fallback=translator)
        self._translator = translator
    return self._translator