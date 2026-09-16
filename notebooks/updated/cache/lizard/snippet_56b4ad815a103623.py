def memoryview_safe(x):
    if not x.flags.writeable:
        if not x.flags.owndata:
            x = x.copy(order='A')
        x.setflags(write=True)
    return x