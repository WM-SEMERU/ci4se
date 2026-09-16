def decode_struct(self, data_type, obj):
    if obj is None and data_type.has_default():
        return data_type.get_default()
    elif not isinstance(obj, dict):
        raise bv.ValidationError('expected object, got %s' % bv.
            generic_type_name(obj))
    all_fields = data_type.definition._all_fields_
    for extra_permission in self.caller_permissions.permissions:
        all_extra_fields = '_all_{}_fields_'.format(extra_permission)
        all_fields = all_fields + getattr(data_type.definition,
            all_extra_fields, [])
    if self.strict:
        all_field_names = data_type.definition._all_field_names_
        for extra_permission in self.caller_permissions.permissions:
            all_extra_field_names = '_all_{}_field_names_'.format(
                extra_permission)
            all_field_names = all_field_names.union(getattr(data_type.
                definition, all_extra_field_names, {}))
        for key in obj:
            if key not in all_field_names and not key.startswith('.tag'):
                raise bv.ValidationError("unknown field '%s'" % key)
    ins = data_type.definition()
    self.decode_struct_fields(ins, all_fields, obj)
    data_type.validate_fields_only_with_permissions(ins, self.
        caller_permissions)
    return ins