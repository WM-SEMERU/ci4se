def get_Tuple_params(tpl):
    try:
        return tpl.__tuple_params__
    except AttributeError:
        try:
            if tpl.__args__ is None:
                return None
            if tpl.__args__[0] == ():
                return ()
            elif tpl.__args__[-1] is Ellipsis:
                return tpl.__args__[:-1] if len(tpl.__args__) > 1 else None
            else:
                return tpl.__args__
        except AttributeError:
            return None