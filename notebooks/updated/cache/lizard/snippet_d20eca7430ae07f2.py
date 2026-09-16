def splitdrive(self, path):
    path = make_string_path(path)
    if self.is_windows_fs:
        if len(path) >= 2:
            path = self.normcase(path)
            sep = self._path_separator(path)
            if sys.version_info >= (2, 7, 8):
                if path[0:2] == sep * 2 and path[2:3] != sep:
                    sep_index = path.find(sep, 2)
                    if sep_index == -1:
                        return path[:0], path
                    sep_index2 = path.find(sep, sep_index + 1)
                    if sep_index2 == sep_index + 1:
                        return path[:0], path
                    if sep_index2 == -1:
                        sep_index2 = len(path)
                    return path[:sep_index2], path[sep_index2:]
            if path[1:2] == self._matching_string(path, ':'):
                return path[:2], path[2:]
    return path[:0], path