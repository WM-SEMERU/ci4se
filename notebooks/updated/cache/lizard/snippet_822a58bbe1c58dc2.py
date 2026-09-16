def _to_dict(self):
    _dict = {}
    if hasattr(self, 'credential_id') and self.credential_id is not None:
        _dict['credential_id'] = self.credential_id
    if hasattr(self, 'source_type') and self.source_type is not None:
        _dict['source_type'] = self.source_type
    if hasattr(self, 'credential_details'
        ) and self.credential_details is not None:
        _dict['credential_details'] = self.credential_details._to_dict()
    return _dict