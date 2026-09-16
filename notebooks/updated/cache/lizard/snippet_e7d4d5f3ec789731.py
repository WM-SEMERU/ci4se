def get_list_of_git_directories():
    dirs = [path[0] for path in list(os.walk('.')) if path[0].endswith('.git')]
    dirs = ['/'.join(path.split('/')[:-1]) for path in dirs]
    return sorted(dirs)