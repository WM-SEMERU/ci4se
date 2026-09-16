def _validate_global_include(self, path):
    if not path.endswith('/'):
        path = os.path.dirname(path)
    if os.path.exists(path):
        if not os.access(path, os.R_OK):
            raise blackbird.utils.error.BlackbirdError(message=
                '{0}: Permission denied.'.format(path))
    else:
        raise blackbird.utils.error.BlackbirdError(message=
            '{0}: No such file or directory.'.format(path))
    return True