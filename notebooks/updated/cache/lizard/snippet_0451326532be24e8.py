def south_field_triple(self):
    from south.modelsinspector import introspector
    try:
        field_class = self.translated_field.south_field_triple()[0]
    except AttributeError:
        field_class = '%s.%s' % (self.translated_field.__class__.__module__,
            self.translated_field.__class__.__name__)
    args, kwargs = introspector(self)
    return field_class, args, kwargs