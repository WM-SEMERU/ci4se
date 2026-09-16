def is_domain(value, **kwargs):
    try:
        value = validators.domain(value, **kwargs)
    except SyntaxError as error:
        raise error
    except Exception:
        return False
    return True