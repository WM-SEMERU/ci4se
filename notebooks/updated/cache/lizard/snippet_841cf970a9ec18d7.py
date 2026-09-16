def __push_import_modules(self):
    for module in self.__import_modules:
        sys.modules[module.__name__] = module