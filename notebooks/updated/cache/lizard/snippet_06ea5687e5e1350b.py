def code_description(self, column=None, value=None, **kwargs):
    return self._resolve_call('PCS_CODE_DESC', column, value, **kwargs)