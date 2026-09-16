def delete(self):
    if not self._ddoc_id:
        raise CloudantArgumentError(125)
    if not self._name:
        raise CloudantArgumentError(126)
    ddoc_id = self._ddoc_id
    if ddoc_id.startswith('_design/'):
        ddoc_id = ddoc_id[8:]
    url = '/'.join((self.index_url, ddoc_id, self._type, self._name))
    resp = self._r_session.delete(url)
    resp.raise_for_status()