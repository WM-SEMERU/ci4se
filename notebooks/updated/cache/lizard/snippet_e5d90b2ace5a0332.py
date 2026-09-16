def is_mac_address(value, **kwargs):
    try:
        value = validators.mac_address(value, **kwargs)
    except SyntaxError as error:
        raise error
    except Exception:
        return False
    return True