def roles(self, clear_features=True, **field_roles):
    field_roles = dict((k, v.name if isinstance(v, SequenceExpr) else v) for
        k, v in six.iteritems(field_roles))
    self._assert_ml_fields_valid(*list(six.itervalues(field_roles)))
    field_roles = dict((_get_field_name(f), MLField.translate_role_name(
        role)) for role, f in six.iteritems(field_roles))
    if field_roles:
        return _change_singleton_roles(self, field_roles, clear_features)
    else:
        return self