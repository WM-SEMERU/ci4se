def _relevant_checkers(self, path):
    _, ext = os.path.splitext(path)
    ext = ext.lstrip('.')
    return checkers.checkers.get(ext, [])