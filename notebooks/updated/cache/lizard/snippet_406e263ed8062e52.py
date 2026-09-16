def delete(self):
    if self._sheet.readonly:
        raise ReadOnlyException
    gd_client = self._sheet.client
    assert gd_client is not None
    return gd_client.DeleteRow(self._entry)