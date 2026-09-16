def is_ip_address(value, **kwargs):
    try:
        value = validators.ip_address(value, **kwargs)
    except SyntaxError as error:
        raise error
    except Exception:
        return False
    return True