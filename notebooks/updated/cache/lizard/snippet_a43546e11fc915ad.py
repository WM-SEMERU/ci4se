def _check_version(version):
    if version != pyphi.__version__:
        raise pyphi.exceptions.JSONVersionError(
            'Cannot load JSON from a different version of PyPhi. JSON version = {0}, current version = {1}.'
            .format(version, pyphi.__version__))