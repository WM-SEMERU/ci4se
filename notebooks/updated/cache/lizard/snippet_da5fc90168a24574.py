def save(self, force_insert=False):
    delayed = {}
    for field, value in self.data.items():
        model_field = getattr(type(self.instance), field, None)
        if isinstance(model_field, ManyToManyField):
            if value is not None:
                delayed[field] = value
            continue
        setattr(self.instance, field, value)
    rv = self.instance.save(force_insert=force_insert)
    for field, value in delayed.items():
        setattr(self.instance, field, value)
    return rv