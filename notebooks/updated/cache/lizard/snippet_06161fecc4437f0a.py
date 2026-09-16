def load_class(cls, identifier, default=None, select=None):
    identifier = identifier.lower()
    key = cls.entry_point, identifier
    if key not in PLUGIN_CACHE:
        if select is None:
            select = default_select
        all_entry_points = list(pkg_resources.iter_entry_points(cls.
            entry_point, name=identifier))
        for extra_identifier, extra_entry_point in cls.extra_entry_points:
            if identifier == extra_identifier:
                all_entry_points.append(extra_entry_point)
        try:
            selected_entry_point = select(identifier, all_entry_points)
        except PluginMissingError:
            if default is not None:
                return default
            raise
        PLUGIN_CACHE[key] = cls._load_class_entry_point(selected_entry_point)
    return PLUGIN_CACHE[key]