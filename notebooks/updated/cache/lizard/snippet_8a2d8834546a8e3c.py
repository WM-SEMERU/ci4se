def normpath(self, path):
    path = self.normcase(path)
    drive, path = self.splitdrive(path)
    sep = self._path_separator(path)
    is_absolute_path = path.startswith(sep)
    path_components = path.split(sep)
    collapsed_path_components = []
    dot = self._matching_string(path, '.')
    dotdot = self._matching_string(path, '..')
    for component in path_components:
        if not component or component == dot:
            continue
        if component == dotdot:
            if collapsed_path_components and collapsed_path_components[-1
                ] != dotdot:
                collapsed_path_components.pop()
                continue
            elif is_absolute_path:
                continue
        collapsed_path_components.append(component)
    collapsed_path = sep.join(collapsed_path_components)
    if is_absolute_path:
        collapsed_path = sep + collapsed_path
    return drive + collapsed_path or dot