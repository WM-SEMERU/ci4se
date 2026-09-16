def base_taskname(taskname, packagename=None):
    if not isinstance(taskname, str):
        return taskname
    indx = taskname.rfind('.')
    if indx >= 0:
        base_taskname = taskname[indx + 1:]
        pkg_name = taskname[:indx]
    else:
        base_taskname = taskname
        pkg_name = ''
    assert True if packagename is None else packagename == pkg_name
    return base_taskname