def takes_instance_or_queryset(func):

    @wraps(func)
    def decorated_function(self, request, queryset):
        if not isinstance(queryset, QuerySet):
            try:
                queryset = self.get_queryset(request).filter(pk=queryset.pk)
            except AttributeError:
                try:
                    model = queryset._meta.model
                except AttributeError:
                    model = queryset._meta.concrete_model
                queryset = model.objects.filter(pk=queryset.pk)
        return func(self, request, queryset)
    return decorated_function