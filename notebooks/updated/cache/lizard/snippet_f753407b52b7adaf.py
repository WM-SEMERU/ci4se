def include_all_subfiles(*args):
    file_list = []
    for path_included in args:
        local_path = path.join(HERE, path_included)
        for file in listdir(local_path):
            file_abspath = path.join(local_path, file)
            if path.isdir(file_abspath):
                continue
            file_list.append(path_included + '/' + file)
    return file_list