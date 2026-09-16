def addobject(bunchdt, data, commdct, key, theidf, aname=None, **kwargs):
    obj = newrawobject(data, commdct, key)
    abunch = obj2bunch(data, commdct, obj)
    if aname:
        namebunch(abunch, aname)
    data.dt[key].append(obj)
    bunchdt[key].append(abunch)
    for key, value in list(kwargs.items()):
        abunch[key] = value
    return abunch