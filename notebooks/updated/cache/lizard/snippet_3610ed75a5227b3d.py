def _to_dict(self):
    _dict = {}
    if hasattr(self, 'name') and self.name is not None:
        _dict['name'] = self.name
    if hasattr(self, 'action_type') and self.action_type is not None:
        _dict['type'] = self.action_type
    if hasattr(self, 'parameters') and self.parameters is not None:
        _dict['parameters'] = self.parameters
    if hasattr(self, 'result_variable') and self.result_variable is not None:
        _dict['result_variable'] = self.result_variable
    if hasattr(self, 'credentials') and self.credentials is not None:
        _dict['credentials'] = self.credentials
    return _dict