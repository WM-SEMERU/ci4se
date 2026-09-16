def get_validated_object(self, value):
    try:
        if self.get_field_type().check_value(value) or self.get_field_type(
            ).can_use_value(value):
            data = self.get_field_type().use_value(value)
            self._prepare_child(data)
            return data
        else:
            return None
    except AttributeError:
        return value