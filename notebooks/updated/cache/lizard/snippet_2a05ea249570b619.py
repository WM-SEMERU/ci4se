def truth(val, context):
    try:
        0 + val
    except TypeError:
        lower_val = val.lower()
        if lower_val in TRUE:
            return True
        elif lower_val in FALSE:
            return False
        else:
            raise FilterError(
                "Bad boolean value %r in %r (expected one of '%s', or '%s')" %
                (val, context, "' '".join(TRUE), "' '".join(FALSE)))
    else:
        return bool(val)