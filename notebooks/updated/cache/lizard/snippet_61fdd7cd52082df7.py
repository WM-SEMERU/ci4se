def findloop(m):
    from _ast import For, While, FunctionDef, ClassDef, ListComp
    from _ast import DictComp
    if isinstance(m, (FunctionDef, ClassDef)):
        return False
    elif isinstance(m, (For, While, ListComp, DictComp)):
        return True
    elif hasattr(m, 'value'):
        return findloop(m.value)
    elif hasattr(m, '__iter__'):
        for sm in m:
            present = findloop(sm)
            if present:
                break
        else:
            present = False
        return present
    elif hasattr(m, 'body') or hasattr(m, 'orelse'):
        body = hasattr(m, 'body') and findloop(m.body)
        orelse = hasattr(m, 'orelse') and findloop(m.orelse)
        return body or orelse
    else:
        return False