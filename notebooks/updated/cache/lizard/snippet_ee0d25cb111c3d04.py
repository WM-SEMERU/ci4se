def list_directories_in_directory(full_directory_path):
    directories = list()
    for directory_name in __os.listdir(full_directory_path):
        if __os.path.isdir(__os.path.join(full_directory_path, directory_name)
            ):
            directories.append(directory_name)
    return directories