def all_files_exist(file_list):
    all_exist = True
    for filename in file_list:
        all_exist = all_exist and os.path.isfile(filename)
    return all_exist