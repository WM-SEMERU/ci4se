def validate(self, value):
    super(ChoiceField, self).validate(value)
    try:
        get_template(value)
    except TemplateDoesNotExist:
        raise ValidationError(_('%s is not a valid template.' % value))