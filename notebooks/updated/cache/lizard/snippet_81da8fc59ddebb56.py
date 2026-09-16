def import_module(modulefn):
    sys.path = [MODULES_FOLDER_PATH] + sys.path
    moduleobj = __import__(modulefn)
    try:
        _attach_module_identifier(moduleobj.moduledata['command_dict'],
            modulefn)
        return moduleobj.moduledata
    except (NameError, KeyError):
        raise seash_exceptions.ModuleImportError("Module '" + modulefn +
            "' is not well defined")
    finally:
        sys.path = sys.path[1:]