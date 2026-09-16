def GetKeyByPath(self, key_path):
    key_path_upper = key_path.upper()
    if key_path_upper.startswith(self._key_path_prefix_upper):
        relative_key_path = key_path[self._key_path_prefix_length:]
    elif key_path.startswith(definitions.KEY_PATH_SEPARATOR):
        relative_key_path = key_path
        key_path = ''.join([self._key_path_prefix, key_path])
    else:
        return None
    path_segments = key_paths.SplitKeyPath(relative_key_path)
    registry_key = self._root_key
    if not registry_key:
        return None
    for path_segment in path_segments:
        registry_key = registry_key.GetSubkeyByName(path_segment)
        if not registry_key:
            return None
    return registry_key