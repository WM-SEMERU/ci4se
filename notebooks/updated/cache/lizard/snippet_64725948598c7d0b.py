def get_external_model(class_object):
    class_abstract = class_object.CodenerixMeta.abstract
    if class_abstract is not None:
        for class_related in class_object._meta.related_objects:
            if issubclass(class_related.related_model, class_abstract):
                return class_related.related_model
    return None