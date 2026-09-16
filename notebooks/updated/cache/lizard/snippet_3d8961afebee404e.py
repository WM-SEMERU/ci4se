def reset():
    global __prefixes_suffixes, __suffixes_to_types, __types, __rule_names_to_types, __target_suffixes_cache
    __register_features()
    __prefixes_suffixes = [property.PropertyMap(), property.PropertyMap()]
    __suffixes_to_types = {}
    __types = {}
    __target_suffixes_cache = {}