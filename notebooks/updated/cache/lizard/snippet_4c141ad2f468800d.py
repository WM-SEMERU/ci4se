def _get_with_default(self, method, section, option, default, expected_type
    =None, **kwargs):
    try:
        try:
            option = option.replace('-', '_')
            return method(self, section, option, **kwargs)
        except (NoOptionError, NoSectionError):
            option_alias = option.replace('_', '-')
            value = method(self, section, option_alias, **kwargs)
            warn = (
                'Configuration [{s}] {o} (with dashes) should be avoided. Please use underscores: {u}.'
                .format(s=section, o=option_alias, u=option))
            warnings.warn(warn, DeprecationWarning)
            return value
    except (NoOptionError, NoSectionError):
        if default is LuigiConfigParser.NO_DEFAULT:
            raise
        if (expected_type is not None and default is not None and not
            isinstance(default, expected_type)):
            raise
        return default