def _to_dict(self):
    _dict = {}
    if hasattr(self, 'level') and self.level is not None:
        _dict['level'] = self.level
    if hasattr(self, 'min_size') and self.min_size is not None:
        _dict['min_size'] = self.min_size
    if hasattr(self, 'max_size') and self.max_size is not None:
        _dict['max_size'] = self.max_size
    if hasattr(self, 'bold') and self.bold is not None:
        _dict['bold'] = self.bold
    if hasattr(self, 'italic') and self.italic is not None:
        _dict['italic'] = self.italic
    if hasattr(self, 'name') and self.name is not None:
        _dict['name'] = self.name
    return _dict