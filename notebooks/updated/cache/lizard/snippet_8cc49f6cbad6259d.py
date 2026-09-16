def find_exe(name):
    for path in os.getenv('PATH').split(os.pathsep):
        for ext in ('', '.exe', '.cmd', '.bat', '.sh'):
            full_path = os.path.join(path, name + ext)
            if os.path.isfile(full_path) and os.access(full_path, os.X_OK):
                return full_path
    return None