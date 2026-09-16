def is_in_file_tree(fpath, folder):
    file_folder, _ = os.path.split(fpath)
    other_folder = os.path.join(folder, '')
    return other_folder.startswith(file_folder)