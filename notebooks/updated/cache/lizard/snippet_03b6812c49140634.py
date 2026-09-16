def deconstruct(self):
    name, path, args, kwargs = super(LocalizedUniqueSlugField, self
        ).deconstruct()
    kwargs['populate_from'] = self.populate_from
    kwargs['include_time'] = self.include_time
    return name, path, args, kwargs