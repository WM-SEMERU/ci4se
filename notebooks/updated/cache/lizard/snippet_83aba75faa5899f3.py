def to_dict(self):

    def transform_value(value):
        if isinstance(value, list):
            return [transform_value(v) for v in value]
        elif isinstance(value, collections.Mapping):
            return dict([(k, transform_value(v)) for k, v in iteritems(value)])
        else:
            return value
    return transform_value(dict(self))