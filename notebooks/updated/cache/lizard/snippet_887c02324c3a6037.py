def _get_all_files(filename_regex, path, base_dir, excluded_paths=None,
    excluded_filename_regex=None):

    def replace_backslashes(string):
        return string.replace('\\', '/')
    excluded_paths = _normalize_excluded_paths(base_dir, excluded_paths)
    if excluded_paths:
        logger.info('Excluding paths: %s', excluded_paths)
    logger.info('Looking for %s under %s...', filename_regex, os.path.join(
        base_dir, path))
    if excluded_filename_regex:
        logger.info('Excluding file names: %s', excluded_filename_regex)
    path_expression = re.compile(replace_backslashes(path))
    target_files = []
    for root, _, files in os.walk(base_dir):
        if not root.startswith(tuple(excluded_paths)
            ) and path_expression.search(replace_backslashes(root)):
            for filename in files:
                filepath = os.path.join(root, filename)
                is_file, matched, excluded_filename, excluded_path = (
                    _set_match_parameters(filename, filepath,
                    filename_regex, excluded_filename_regex, excluded_paths))
                if (is_file and matched and not excluded_filename and not
                    excluded_path):
                    logger.debug('%s is a match. Appending to list...',
                        filepath)
                    target_files.append(filepath)
    return target_files