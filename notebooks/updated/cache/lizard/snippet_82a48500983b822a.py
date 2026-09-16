def createEdge(self, collectionName, _fromId, _toId, edgeAttributes,
    waitForSync=False):
    if not _fromId:
        raise ValueError('Invalid _fromId: %s' % _fromId)
    if not _toId:
        raise ValueError('Invalid _toId: %s' % _toId)
    if collectionName not in self.definitions:
        raise KeyError("'%s' is not among the edge definitions" %
            collectionName)
    url = '%s/edge/%s' % (self.URL, collectionName)
    self.database[collectionName].validatePrivate('_from', _fromId)
    self.database[collectionName].validatePrivate('_to', _toId)
    ed = self.database[collectionName].createEdge()
    ed.set(edgeAttributes)
    ed.validate()
    payload = ed.getStore()
    payload.update({'_from': _fromId, '_to': _toId})
    r = self.connection.session.post(url, data=json.dumps(payload, default=
        str), params={'waitForSync': waitForSync})
    data = r.json()
    if r.status_code == 201 or r.status_code == 202:
        return self.database[collectionName][data['edge']['_key']]
    raise CreationError('Unable to create edge, %s' % r.json()[
        'errorMessage'], data)