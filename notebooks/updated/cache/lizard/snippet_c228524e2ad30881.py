def FromString(self, string):
    if string.lower() in ('false', 'no', 'n'):
        return False
    if string.lower() in ('true', 'yes', 'y'):
        return True
    raise TypeValueError('%s is not recognized as a boolean value.' % string)