def _read(self, directory, filename, session, path, name, extension,
    spatial, spatialReferenceID, replaceParamFile):
    self.fileExtension = extension
    KEYWORDS = 'EVENT',
    with open(path, 'r') as f:
        chunks = pt.chunk(KEYWORDS, f)
    for key, chunkList in iteritems(chunks):
        for chunk in chunkList:
            result = gak.eventChunk(key, chunk)
            self._createGsshaPyObjects(result)
    session.add(self)