def chkdeps(*args):
    module_names = args
    if len(module_names) <= 0:
        error('No module specified')
        return
    distribution = get_distribution()
    for module_name in module_names:
        _chkdeps(module_name, distribution)