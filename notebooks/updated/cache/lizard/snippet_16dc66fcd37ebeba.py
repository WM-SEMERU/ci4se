def __parameter_default(self, field):
    if field.default:
        if isinstance(field, messages.EnumField):
            return field.default.name
        elif isinstance(field, messages.BooleanField):
            return 'true' if field.default else 'false'
        else:
            return str(field.default)