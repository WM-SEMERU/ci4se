def _validate_field_can_be_tagged_with_redactor(self, field):
    if is_alias(field.data_type):
        raise InvalidSpec(
            'Redactors can only be applied to alias definitions, not to alias references.'
            , field._ast_node.lineno, field._ast_node.path)
    self._validate_object_can_be_tagged_with_redactor(field)