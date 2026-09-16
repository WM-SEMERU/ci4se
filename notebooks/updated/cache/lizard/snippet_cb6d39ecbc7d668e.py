def _initialize_referenced(model_class, attribute):

    def _related_objects(self):
        return model_class.objects.filter(**{attribute.attname: self.id})
    klass = attribute._target_type
    if isinstance(klass, basestring):
        return klass, model_class, attribute
    else:
        related_name = attribute.related_name or model_class.__name__.lower(
            ) + '_set'
        setattr(klass, related_name, property(_related_objects))