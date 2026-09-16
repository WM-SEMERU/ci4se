def _get_programs_dict():
    global __programs_dict
    if __programs_dict is not None:
        return __programs_dict
    d = __programs_dict = OrderedDict()
    for pkgname in COLLABORATORS_S:
        try:
            package = importlib.import_module(pkgname)
        except ImportError:
            continue
        path_ = os.path.join(os.path.split(package.__file__)[0], 'scripts')
        bulk = a99.get_exe_info(path_, flag_protected=True)
        d[pkgname] = {'description': a99.get_obj_doc0(package), 'exeinfo': bulk
            }
    return __programs_dict