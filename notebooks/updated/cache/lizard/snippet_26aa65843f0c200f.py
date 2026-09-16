def find_file(path_dir, search_str, file_ext):
    import os
    file_path = None
    for file_name in os.listdir(path_dir):
        if search_str in file_name and file_name.endswith(file_ext):
            file_path = os.path.join(path_dir, file_name)
            break
    if file_path == None:
        raise SystemError('No file found containing string: {}.'.format(
            search_str))
    return file_path