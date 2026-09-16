def get_folder_list(folder='.'):
    dir_list = get_content_list(folder)
    return [f for f in dir_list if not os.path.isfile(os.path.join(folder, f))]