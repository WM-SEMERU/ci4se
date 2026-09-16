def is_domterm(cls):
    import os
    if cls._is_domterm is not None:
        return cls._is_domterm
    if not os.environ.get('DOMTERM'):
        cls._is_domterm = False
        return False
    cls._is_domterm = True
    return True