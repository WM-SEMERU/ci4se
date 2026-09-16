def _to_dict(self):
    _dict = {}
    if hasattr(self, 'path') and self.path is not None:
        _dict['path'] = self.path
    return _dict