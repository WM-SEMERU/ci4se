def discover_by_module(self, module_name, top_level_directory=None, pattern
    ='test*.py'):
    if top_level_directory is not None and top_level_directory not in sys.path:
        sys.path.insert(0, top_level_directory)
    logger.debug(
        'Discovering tests by module: module_name=%r, top_level_directory=%r, pattern=%r'
        , module_name, top_level_directory, pattern)
    try:
        module, case_attributes = find_module_by_name(module_name)
    except ImportError:
        return self.discover_filtered_tests(module_name,
            top_level_directory=top_level_directory, pattern=pattern)
    dirname, basename = os.path.split(module.__file__)
    basename = os.path.splitext(basename)[0]
    if len(case_attributes) == 0 and basename == '__init__':
        return self.discover_by_directory(dirname, top_level_directory,
            pattern=pattern)
    elif len(case_attributes) == 0:
        return self._loader.load_module(module)
    return self.discover_single_case(module, case_attributes)