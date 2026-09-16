def trace_modules(self, modules, pattern='.*', flags=re.IGNORECASE):
    try:
        pattern = re.compile(pattern, flags)
    except Exception:
        raise foundations.exceptions.UserError(
            '{0} | Invalid objects trace filter pattern: Regex compilation failed!'
            .format(self.__class__.__name__))
    for module in modules:
        foundations.trace.trace_module(module, foundations.verbose.tracer,
            pattern)
    self.__model__refresh_attributes()
    return True