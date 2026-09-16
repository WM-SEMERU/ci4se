def unregister(self, model_or_iterable):
    if isinstance(model_or_iterable, ModelBase):
        model_or_iterable = [model_or_iterable]
    for model in model_or_iterable:
        if model not in self._registry:
            raise NotModerated(
                "The model '%s' is not currently being moderated" % model.
                _meta.module_name)
        del self._registry[model]