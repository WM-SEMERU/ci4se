def get_files_from_dir(path, recursive=True, depth=0, file_ext='.py'):
    file_list = []
    if os.path.isfile(path) or path == '-':
        return [path]
    if path[-1] != os.sep:
        path = path + os.sep
    for f in glob.glob(path + '*'):
        if os.path.isdir(f):
            if depth < MAX_DEPTH_RECUR:
                file_list.extend(get_files_from_dir(f, recursive, depth + 1))
            else:
                continue
        elif f.endswith(file_ext):
            file_list.append(f)
    return file_list