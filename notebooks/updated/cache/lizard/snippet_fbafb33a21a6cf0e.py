def convertfields(key_comm, obj, inblock=None):
    convinidd = ConvInIDD()
    if not inblock:
        inblock = ['does not start with N'] * len(obj)
    for i, (f_comm, f_val, f_iddname) in enumerate(zip(key_comm, obj, inblock)
        ):
        if i == 0:
            pass
        else:
            obj[i] = convertafield(f_comm, f_val, f_iddname)
    return obj