def getbool(value):
    value = str(value).lower()
    if value in ['1', 't', 'true', 'y', 'yes']:
        return True
    elif value in ['0', 'f', 'false', 'n', 'no']:
        return False
    return None