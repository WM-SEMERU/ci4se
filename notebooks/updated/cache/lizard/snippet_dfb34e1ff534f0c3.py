def result(self):
    try:
        r = getattr(self, '_result')
    except AttributeError:
        return None
    else:
        if hasattr(self, '_exception'):
            raise self._exception
        else:
            return r