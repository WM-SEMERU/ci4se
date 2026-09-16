def field_factory(base_class):
    from .fields import TranslationField


    class TranslationFieldField(TranslationField, base_class):
        pass
    TranslationFieldField.__name__ = 'Translation%s' % base_class.__name__
    return TranslationFieldField