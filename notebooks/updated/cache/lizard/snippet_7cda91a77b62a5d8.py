def _GeneratePathString(self, mediator, pathspec, hashes):
    display_name = mediator.GetDisplayNameForPathSpec(pathspec)
    path_string = '{0:s}:'.format(display_name)
    for hash_name, hash_value in sorted(hashes.items()):
        path_string = '{0:s} {1:s}={2:s}'.format(path_string, hash_name,
            hash_value)
    return path_string