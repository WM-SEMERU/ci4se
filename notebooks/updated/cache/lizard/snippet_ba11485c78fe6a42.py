def get_queryset(self):
    if self.queryset is None and not self.model:
        try:
            ModelClass = apps.get_model(self.kwargs.get('app'), self.kwargs
                .get('model'))
            return ModelClass._default_manager.all()
        except LookupError:
            raise Http404()
    return super().get_queryset()