def ecn(ns=None, cn=None, di=None):
    return CONN.EnumerateClassNames(ns, ClassName=cn, DeepInheritance=di)