def to_bool(self, value):
    try:
        value = value.lower()
    except:
        pass
    try:
        value = value.encode('utf-8')
    except:
        pass
    try:
        value = int(value)
    except:
        pass
    if value in ('true', 1):
        return True
    else:
        return False