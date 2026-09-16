def get(self, *args, **kwargs):
    assert not args
    assert list(kwargs.keys()) == ['pk']
    pk = kwargs['pk']
    model_name = self.model.__name__
    object_spec = model_name, pk, None
    instances = self.cache.get_instances((object_spec,))
    try:
        model_data = instances[model_name, pk][0]
    except KeyError:
        raise self.model.DoesNotExist(
            'No match for %r with args %r, kwargs %r' % (self.model, args,
            kwargs))
    else:
        return CachedModel(self.model, model_data)