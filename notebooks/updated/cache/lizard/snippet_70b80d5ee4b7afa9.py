def register(cls, attr_name, attr_cls):
    if not cls.INSERT_AFTER_FIELD:
        raise ValueError('Class %s is missing INSERT_AFTER_FIELD value' % cls)
    try:
        cls.get_field_by_fieldname(attr_name)
    except InvalidField:
        pass
    else:
        raise ValueError("'%s' is already registered" % attr_name)
    if not issubclass(attr_cls, ExtendedProperty):
        raise ValueError('%r must be a subclass of ExtendedProperty' % attr_cls
            )
    attr_cls.validate_cls()
    field = ExtendedPropertyField(attr_name, value_cls=attr_cls)
    cls.add_field(field, insert_after=cls.INSERT_AFTER_FIELD)