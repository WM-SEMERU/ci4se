def _to_dict(self):
    _dict = {}
    if hasattr(self, 'overwrite') and self.overwrite is not None:
        _dict['overwrite'] = self.overwrite
    return _dict