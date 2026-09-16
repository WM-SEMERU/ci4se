def law_home_path(*paths):
    home = os.getenv('LAW_HOME', '$HOME/.law')
    home = os.path.expandvars(os.path.expanduser(home))
    return os.path.normpath(os.path.join(home, *paths))