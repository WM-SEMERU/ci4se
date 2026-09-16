def TemplateValidator(value):
    try:
        Template(value)
    except Exception as e:
        raise ValidationError(_('Cannot compile template (%(exception)s)'),
            params={'exception': e})