def schema_factory(schema_name, **schema_nodes):
    schema_dict = dict()
    schema_dict.update(schema_nodes)

    def cls_repr(self):
        return '<{} instance at: 0x{:x}>'.format(self.__class__, id(self))

    def cls_str(self):
        return '<{} instance, attributes:{}>'.format(self.__class__.
            __name__, self.schema_nodes)

    def cls_init(self, **kwargs):
        kwargs_set = set(kwargs)
        if not self.required.issubset(kwargs_set):
            raise SchemaError('Missing Required Attributes: {}'.format(self
                .required.difference(kwargs_set)))
        if not set(kwargs).issubset(set(self.schema_nodes)):
            raise SchemaError('Invalid Attributes {} for {}.'.format(self.
                __class__.__name__, set(kwargs).difference(set(self.
                schema_nodes))))
        for attr_name in kwargs:
            setattr(self, attr_name, kwargs[attr_name])

    def to_dict(self):
        return OrderedDict([(k, getattr(self, k)) for k in self.schema_nodes])
    schema_dict['to_dict'] = property(to_dict)
    schema_dict['__init__'] = cls_init
    schema_dict['__repr__'] = cls_repr
    schema_dict['__str__'] = cls_str
    return SchemaType('{}Schema'.format(schema_name.title()), (), schema_dict)