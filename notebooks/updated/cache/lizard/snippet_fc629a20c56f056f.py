def _to_dict(self):
    _dict = {}
    if hasattr(self, 'collections') and self.collections is not None:
        _dict['collections'] = [x._to_dict() for x in self.collections]
    return _dict