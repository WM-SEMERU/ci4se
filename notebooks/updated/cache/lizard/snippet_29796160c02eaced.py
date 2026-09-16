def validate_fields_only_with_permissions(self, val, caller_permissions):
    self.validate_fields_only(val)
    for extra_permission in caller_permissions.permissions:
        all_field_names = '_all_{}_field_names_'.format(extra_permission)
        for field_name in getattr(self.definition, all_field_names, set()):
            if not hasattr(val, field_name):
                raise ValidationError("missing required field '%s'" %
                    field_name)