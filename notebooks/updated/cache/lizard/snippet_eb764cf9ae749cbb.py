def _to_dict(self):
    _dict = {}
    if hasattr(self, 'features') and self.features is not None:
        _dict['features'] = self.features
    if hasattr(self, 'text_characters') and self.text_characters is not None:
        _dict['text_characters'] = self.text_characters
    if hasattr(self, 'text_units') and self.text_units is not None:
        _dict['text_units'] = self.text_units
    return _dict