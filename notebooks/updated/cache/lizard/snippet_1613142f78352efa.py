def is_type(type_, *p):
    try:
        for i in p:
            if i.type_ != type_:
                return False
        return True
    except:
        pass
    return False