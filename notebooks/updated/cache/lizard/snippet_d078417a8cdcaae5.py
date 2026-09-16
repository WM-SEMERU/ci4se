def _assert_in_buildroot(self, filepath):
    filepath = os.path.normpath(filepath)
    root = get_buildroot()
    if not os.path.abspath(filepath) == filepath:
        return os.path.join(root, filepath)
    else:
        if '..' in os.path.relpath(filepath, root).split(os.path.sep):
            raise ValueError(
                """Received a file_option that was not inside the build root:
  file_option: {filepath}
  build_root:  {buildroot}
"""
                .format(filepath=filepath, buildroot=root))
        return filepath