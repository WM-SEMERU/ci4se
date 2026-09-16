def constraint_from_choices(cls, value_type: type, choices: collections.
    Sequence):
    choices_str = ', '.join(map(str, choices))

    def constraint(value):
        value = value_type(value)
        if value not in choices:
            raise ParameterError('Argument must be one of %s' % choices_str)
        return value
    constraint.__name__ = 'choices_%s' % value_type.__name__
    constraint.__doc__ = 'choice of %s' % choices_str
    return constraint