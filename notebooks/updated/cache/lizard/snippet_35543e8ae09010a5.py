def build_info(name, path=None, module=None):
    verlist = get_version_list(path, module)
    verlist[0] = name
    return tuple(verlist)