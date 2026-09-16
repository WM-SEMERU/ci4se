def is_fraction(value, minimum=None, maximum=None, **kwargs):
    try:
        value = validators.fraction(value, minimum=minimum, maximum=maximum,
            **kwargs)
    except SyntaxError as error:
        raise error
    except Exception:
        return False
    return True