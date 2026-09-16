def get_object(self, request, object_id):
    queryset = self.queryset(request)
    model = queryset.model
    try:
        object_id = model._meta.pk.to_python(object_id)
        return queryset.get(pk=object_id)
    except (model.DoesNotExist, ValidationError):
        return None