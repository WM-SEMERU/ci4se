def _import_all_troposphere_modules(self):
    dirname = os.path.join(os.path.dirname(__file__))
    module_names = [pkg_name for importer, pkg_name, is_pkg in pkgutil.
        walk_packages([dirname], prefix='troposphere.') if not is_pkg and 
        pkg_name not in self.EXCLUDE_MODULES]
    module_names.append('troposphere')
    modules = []
    for name in module_names:
        modules.append(importlib.import_module(name))

    def members_predicate(m):
        return inspect.isclass(m) and not inspect.isbuiltin(m)
    members = []
    for module in modules:
        members.extend(m[1] for m in inspect.getmembers(module,
            members_predicate))
    return set(members)