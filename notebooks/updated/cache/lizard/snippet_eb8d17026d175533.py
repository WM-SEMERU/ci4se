def GetIpForwardTable():
    size = ULONG()
    res = _GetIpForwardTable(None, byref(size), False)
    if res != 122:
        raise RuntimeError('Error getting structure length (%d)' % res)
    pointer_type = PMIB_IPFORWARDTABLE
    buffer = create_string_buffer(size.value)
    pIpForwardTable = ctypes.cast(buffer, pointer_type)
    res = _GetIpForwardTable(pIpForwardTable, byref(size), True)
    if res != NO_ERROR:
        raise RuntimeError('Error retrieving table (%d)' % res)
    results = []
    for i in range(pIpForwardTable.contents.NumEntries):
        results.append(_struct_to_dict(pIpForwardTable.contents.Table[i]))
    del pIpForwardTable
    return results