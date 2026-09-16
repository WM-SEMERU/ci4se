def get_pyof_version(module_fullname):
    ver_module_re = re.compile('(pyof\\.)(v0x\\d+)(\\..*)')
    matched = ver_module_re.match(module_fullname)
    if matched:
        version = matched.group(2)
        return version
    return None