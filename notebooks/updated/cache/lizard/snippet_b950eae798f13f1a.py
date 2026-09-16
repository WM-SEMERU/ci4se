def _find_file(self, needle, candidates):
    for candidate in candidates:
        fullpath = os.path.join(candidate, needle)
        if os.path.isfile(fullpath):
            return fullpath
    raise PathError('Unable to locate file %s; tried %s' % (needle, candidates)
        )