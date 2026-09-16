def validate(self, require_all=True, scale='colors'):
    super(self.__class__, self).validate()
    required_attribs = 'data', 'scales', 'axes', 'marks'
    for elem in required_attribs:
        attr = getattr(self, elem)
        if attr:
            for entry in attr:
                entry.validate()
            names = [a.name for a in attr]
            if len(names) != len(set(names)):
                raise ValidationError(elem + ' has duplicate names')
        elif require_all:
            raise ValidationError(elem +
                ' must be defined for valid visualization')