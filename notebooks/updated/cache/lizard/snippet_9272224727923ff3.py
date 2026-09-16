def _deconstruct_binary(self, data):
    attachments = []
    data = self._deconstruct_binary_internal(data, attachments)
    return data, attachments