def getbool(key, default=False):
    value = os.getenv(key)
    if value and value.lower() in ('true', '1'):
        value = True
    elif value and value.lower() in ('false', '0'):
        value = False
    else:
        value = default
    return value