def DeregisterSourceType(cls, source_type_class):
    if source_type_class.TYPE_INDICATOR not in cls._source_type_classes:
        raise KeyError('Source type not set for type: {0:s}.'.format(
            source_type_class.TYPE_INDICATOR))
    del cls._source_type_classes[source_type_class.TYPE_INDICATOR]