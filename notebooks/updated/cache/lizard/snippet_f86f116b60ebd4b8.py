def find_sanitizer(self, name):
    name_parts = name.split('.')
    if len(name_parts) < 2:
        raise ConfigurationError(
            "Unable to separate module name from function name in '%s'" % (
            name,))
    module_name_suffix = '.'.join(name_parts[:-1])
    function_name = 'sanitize_%s' % (name_parts[-1],)
    module_name = 'sanitizers.%s' % (module_name_suffix,)
    callback = self.find_sanitizer_from_module(module_name=module_name,
        function_name=function_name)
    if callback:
        return callback
    for addon_package_name in self.addon_packages:
        module_name = '%s.%s' % (addon_package_name, module_name_suffix)
        callback = self.find_sanitizer_from_module(module_name=module_name,
            function_name=function_name)
        if callback:
            return callback
    module_name = 'database_sanitizer.sanitizers.%s' % (module_name_suffix,)
    callback = self.find_sanitizer_from_module(module_name=module_name,
        function_name=function_name)
    if callback:
        return callback
    raise ConfigurationError("Unable to find sanitizer called '%s'" % (name,))