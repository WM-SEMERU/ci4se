def create_symlink(local_file, symlink_path):
    if symlink_path is not None:
        if os.path.exists(symlink_path) or os.path.lexists(symlink_path):
            os.unlink(symlink_path)
        local_file = os.path.normpath(local_file)
        symlink_path = os.path.normpath(symlink_path)
        num_dirs_upward = len(os.path.dirname(symlink_path).split(os.sep))
        local_relative_to_symlink = num_dirs_upward * (os.pardir + os.sep)
        os.symlink(os.path.join(local_relative_to_symlink, local_file),
            symlink_path)
    return True