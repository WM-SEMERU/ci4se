def _maybe_replace_path(self, match):
    path = match.group(0)
    if self._should_replace(path):
        return self._replace_path(path)
    else:
        return path