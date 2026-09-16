def update_model_languages(self, model_class, languages):
    qs = TransLanguage.objects.filter(code__in=languages)
    new_langs = [lang for lang in qs]
    if not new_langs:
        return
    mod_lan, created = TransModelLanguage.objects.get_or_create(model=
        '{} - {}'.format(model_class._meta.app_label, model_class._meta.
        model.__name__.lower()))
    exist_langs_codes = [lang.code for lang in mod_lan.languages.all()]
    for lang in new_langs:
        if lang.code not in exist_langs_codes:
            try:
                mod_lan.languages.add(lang)
            except IntegrityError:
                pass