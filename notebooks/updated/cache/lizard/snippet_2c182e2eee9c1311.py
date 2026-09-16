def PrepareMatches(self, file_system):
    if self._location is not None:
        self._location_segments = self._SplitPath(self._location,
            file_system.PATH_SEPARATOR)
    elif self._location_regex is not None:
        path_separator = file_system.PATH_SEPARATOR
        if path_separator == '\\':
            path_separator = '\\\\'
        self._location_segments = self._SplitPath(self._location_regex,
            path_separator)
    if self._location_segments is not None:
        self._number_of_location_segments = len(self._location_segments)