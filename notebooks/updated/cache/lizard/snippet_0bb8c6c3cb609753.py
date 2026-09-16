def import_code(mod_code, mod_name):
    mod_obj = imp.new_module(mod_name)
    mod_obj.__file__ = None
    exec_(mod_code, mod_obj.__dict__, mod_obj.__dict__)
    add_to_sys_modules(mod_name=mod_name, mod_obj=mod_obj)
    return mod_obj