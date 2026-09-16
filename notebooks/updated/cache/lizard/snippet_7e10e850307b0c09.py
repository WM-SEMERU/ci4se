def IE_Dispatcher(s):
    if len(s) < 1:
        return Raw(s)
    ietype = ord(s[0])
    cls = ietypecls.get(ietype, Raw)
    if cls == Raw and ietype & 128 == 128:
        cls = IE_NotImplementedTLV
    return cls(s)