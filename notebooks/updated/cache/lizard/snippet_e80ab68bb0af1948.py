def reftrack_rtype_data(rt, role):
    tfi = rt.get_taskfileinfo()
    if not tfi:
        return
    return filesysitemdata.taskfileinfo_rtype_data(tfi, role)