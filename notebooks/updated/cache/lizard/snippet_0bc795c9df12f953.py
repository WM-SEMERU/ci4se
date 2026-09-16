def _formatter_self(name, value):
    __mname = value.__module__
    if __mname != '__main__':
        return '%s = <%s.%s object at 0x%x>' % (name, __mname, value.
            __class__.__name__, id(value))
    else:
        return '%s = <%s object at 0x%x>' % (name, value.__class__.__name__,
            id(value))