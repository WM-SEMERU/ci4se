def get_queryset(self, request):
    qs = super(BaseTranslatableAdmin, self).get_queryset(request)
    if self._has_translatable_model():
        if not isinstance(qs, TranslatableQuerySet):
            raise ImproperlyConfigured(
                '{0} class does not inherit from TranslatableQuerySet'.
                format(qs.__class__.__name__))
        qs_language = self.get_queryset_language(request)
        if qs_language:
            qs = qs.language(qs_language)
    return qs