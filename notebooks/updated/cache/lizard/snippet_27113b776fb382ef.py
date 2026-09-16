def update_translations(condition=None):
    if condition is None:
        condition = {}
    num_translations = 0
    FieldTranslation._init_module_cache()
    LANGUAGES = dict(lang for lang in MODELTRANSLATION_LANG_CHOICES)
    if settings.LANGUAGE_CODE in LANGUAGES:
        del LANGUAGES[settings.LANGUAGE_CODE]
    for key in FieldTranslation._modules.keys():
        module = FieldTranslation._modules[key]
        clsmembers = inspect.getmembers(sys.modules[key], inspect.isclass)
        for cls in clsmembers:
            cls = cls[1]
            if hasattr(cls, '_meta') and not cls._meta.abstract and hasattr(cls
                ._meta, 'translatable_fields') and len(cls._meta.
                translatable_fields) > 0:
                objects = cls.objects.filter(**condition)
                for obj in objects:
                    for lang in LANGUAGES.keys():
                        for field in cls._meta.translatable_fields:
                            if FieldTranslation.update(obj=obj, field=field,
                                lang=lang, context=''):
                                num_translations += 1
    return num_translations