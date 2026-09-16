def getOSDesc(interface, ext_list):
    try:
        ext_type, = {type(x) for x in ext_list}
    except ValueError:
        raise TypeError('Extensions of a single type are required.')
    if issubclass(ext_type, OSExtCompatDesc):
        wIndex = 4
        kw = {'b': OSDescHeaderBCount(bCount=len(ext_list), Reserved=0)}
    elif issubclass(ext_type, OSExtPropDescHead):
        wIndex = 5
        kw = {'wCount': len(ext_list)}
    else:
        raise TypeError('Extensions of unexpected type')
    ext_list_type = ext_type * len(ext_list)
    klass = type('OSDesc', (OSDescHeader,), {'_fields_': [('ext_list',
        ext_list_type)]})
    return klass(interface=interface, dwLength=ctypes.sizeof(klass),
        bcdVersion=1, wIndex=wIndex, ext_list=ext_list_type(*ext_list), **kw)