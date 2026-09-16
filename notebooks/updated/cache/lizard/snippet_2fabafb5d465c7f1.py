def _check_states_enum(cls):
    states_enum_name = cls.context.get_config('states_enum_name')
    try:
        cls.context['states_enum'] = getattr(cls.context.new_class,
            states_enum_name)
    except AttributeError:
        raise ValueError('No states enum given!')
    proper = True
    try:
        if not issubclass(cls.context.states_enum, Enum):
            proper = False
    except TypeError:
        proper = False
    if not proper:
        raise ValueError(
            'Please provide enum instance to define available states.')