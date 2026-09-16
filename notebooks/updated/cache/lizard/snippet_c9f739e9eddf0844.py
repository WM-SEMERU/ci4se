def validate(self, value):
    if self.exclusive:
        if value >= self.maximum_value:
            tpl = "'{val}' is bigger or equal than maximum ('{max}')."
            raise ValidationError(tpl.format(val=value, max=self.maximum_value)
                )
    elif value > self.maximum_value:
        raise ValidationError("'{value}' is bigger than maximum ('{max}')."
            .format(value=value, max=self.maximum_value))