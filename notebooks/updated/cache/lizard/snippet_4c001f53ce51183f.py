def _build_folder_tree(top_abspath, followsymlinks, file_filter):
    path_to_content = {}
    child_to_parent = {}
    ignore_file_patterns = IgnoreFilePatterns(file_filter)
    ignore_file_patterns.load_directory(top_abspath, followsymlinks)
    for dir_name, child_dirs, child_files in os.walk(top_abspath,
        followlinks=followsymlinks):
        abspath = os.path.abspath(dir_name)
        folder = LocalFolder(abspath)
        path_to_content[abspath] = folder
        parent_path = child_to_parent.get(abspath)
        if parent_path:
            path_to_content[parent_path].add_child(folder)
        remove_child_dirs = []
        for child_dir in child_dirs:
            abs_child_path = os.path.abspath(os.path.join(dir_name, child_dir))
            if ignore_file_patterns.include(abs_child_path, is_file=False):
                child_to_parent[abs_child_path] = abspath
            else:
                remove_child_dirs.append(child_dir)
        for remove_child_dir in remove_child_dirs:
            child_dirs.remove(remove_child_dir)
        for child_filename in child_files:
            abs_child_filename = os.path.join(dir_name, child_filename)
            if ignore_file_patterns.include(abs_child_filename, is_file=True):
                folder.add_child(LocalFile(abs_child_filename))
    return path_to_content.get(top_abspath)