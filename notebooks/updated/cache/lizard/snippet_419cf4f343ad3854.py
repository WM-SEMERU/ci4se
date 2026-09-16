def pclass_field_for_attribute(self):
    return self.type_model.pclass_field_for_type(required=self.required,
        default=self.default)