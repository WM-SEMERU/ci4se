def _CheckIfPathIsValidForDeletion(path, prefix=None, directories=None):
    precondition.AssertType(path, Text)
    precondition.AssertType(prefix, Text)
    if prefix and os.path.basename(path).startswith(prefix):
        return True
    path = path.lower()
    for directory in (directories or []):
        directory = directory.lower()
        if os.path.commonprefix([directory, path]) == directory:
            return True
    return False