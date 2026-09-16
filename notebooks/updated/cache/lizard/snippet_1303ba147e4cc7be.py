def set_field_value(self, field_name, value):
    self.view._json_params[field_name] = value
    if field_name in self.fields:
        self.fields[field_name].new_value = value
        return
    fields = FieldData.from_dict({field_name: value}, self.model)
    self.fields.update(fields)