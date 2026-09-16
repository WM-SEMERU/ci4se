def relative_path(cls, git_diff_path):
    root_rel_path = os.path.relpath(cls._cwd, cls._root)
    rel_path = os.path.relpath(git_diff_path, root_rel_path)
    return rel_path