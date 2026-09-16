def get_all_tags_and_filters_by_function():
    libraries = get_template_libraries()
    force = False
    if hasattr(CacheTag.get_all_tags_and_filters_by_function, '_len_libraries'
        ):
        if len(libraries
            ) != CacheTag.get_all_tags_and_filters_by_function._len_libraries:
            force = True
    if force or not hasattr(CacheTag.get_all_tags_and_filters_by_function,
        '_cache'):
        CacheTag.get_all_tags_and_filters_by_function._len_libraries = len(
            libraries)
        available_tags = {}
        available_filters = {}
        for lib_name, lib in libraries.items():
            available_tags.update((function, (lib_name, tag_name)) for 
                tag_name, function in lib.tags.items())
            available_filters.update((function, (lib_name, filter_name)) for
                filter_name, function in lib.filters.items())
        CacheTag.get_all_tags_and_filters_by_function._cache = {'tags':
            available_tags, 'filters': available_filters}
    return CacheTag.get_all_tags_and_filters_by_function._cache