def make_folder(path):
    if not os.path.exists(path):
        try:
            os.makedirs(path)
        except OSError as exception:
            if exception.errno != errno.EEXIST:
                raise ValueError(
                    """Specified folder is not writable: %s
Please check permissions or set a new valid folder."""
                     % path)