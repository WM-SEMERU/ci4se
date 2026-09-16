def validation_error_message(cls, spec, backends=None):
    try:
        cls.validate_spec(spec, backends=backends)
    except OptionError as e:
        return e.format_options_error()