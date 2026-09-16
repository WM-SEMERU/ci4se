def _all_help_methods(self):
    methods = {name: method for name, method in inspect.getmembers(self,
        predicate=inspect.isroutine) if not name.startswith('_')}
    return methods