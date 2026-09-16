def find(cls, searched_dir, pattern):
    Log.debug('find {0} with pattern: {1}'.format(searched_dir, pattern))
    matched_files = []
    for root_dir, dir_names, file_names in os.walk(searched_dir,
        followlinks=False):
        for file_name in file_names:
            if fnmatch.fnmatch(file_name, pattern):
                file_path = os.path.join(root_dir, file_name)
                if not os.path.islink(file_path):
                    matched_files.append(file_path)
    matched_files.sort()
    return matched_files