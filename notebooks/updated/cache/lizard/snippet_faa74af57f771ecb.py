def _bind_field(self, field_name, field_obj):
    try:
        if field_name in self.load_only:
            field_obj.load_only = True
        if field_name in self.dump_only:
            field_obj.dump_only = True
        field_obj._bind_to_schema(field_name, self)
        self.on_bind_field(field_name, field_obj)
    except TypeError:
        if isinstance(field_obj, type) and issubclass(field_obj, base.FieldABC
            ):
            msg = (
                'Field for "{}" must be declared as a Field instance, not a class. Did you mean "fields.{}()"?'
                .format(field_name, field_obj.__name__))
            raise TypeError(msg)