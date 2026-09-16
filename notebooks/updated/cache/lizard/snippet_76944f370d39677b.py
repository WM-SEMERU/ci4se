def add_default_argument(self, name, value_type, item_help, default=None):
    if value_type not in self.__restricted_default_types:
        raise ArgumentException(
            "Positional(default) argument couldn't have {} type".format(
            value_type.__name__))
    if self.__is_default_arg_flag_used and default is None:
        raise ArgumentException(
            'After defining first default Positional argument, rest should have default value too'
            .format(value_type.__name__))
    elif default is not None:
        self.__is_default_arg_flag_used = True
        if not isinstance(default, value_type):
            raise ArgumentException('Invalid default type for argument'.
                format(name))
    self._default_args.append(ModuleArgumentItem(name, value_type,
        item_help, default=default))
    return self