def make_modules(self, groups, code_opts):
    modules = []
    for raw_module, raw_funcs in groups:
        module = raw_module[0].strip().strip(string.punctuation)
        funcs = [func.strip() for func in raw_funcs]
        args = [self.database.query_args(func, raw=True) for func in funcs]
        if self.generic:
            args = [(arg if arg else ('VOID *', [])) for arg in args]
        else:
            args = [arg for arg in args if arg]
        if not args:
            logging.info(_('%s not found.'), module)
            continue
        logging.debug(module)
        module = ModuleSource(module, zip(funcs, args), code_opts)
        modules.append(module.c_source())
    return AttrsGetter(modules)