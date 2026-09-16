def links(self, fromVertice, toVertice, **edgeArgs):
    if isinstance(fromVertice, Document) or isinstance(getattr(fromVertice,
        'document', None), Document):
        if not fromVertice._id:
            fromVertice.save()
        self._from = fromVertice._id
    elif type(fromVertice) is bytes or type(fromVertice) is str:
        self._from = fromVertice
    elif not self._from:
        raise CreationError('fromVertice %s is invalid!' % str(fromVertice))
    if isinstance(toVertice, Document) or isinstance(getattr(toVertice,
        'document', None), Document):
        if not toVertice._id:
            toVertice.save()
        self._to = toVertice._id
    elif type(toVertice) is bytes or type(toVertice) is str:
        self._to = toVertice
    elif not self._to:
        raise CreationError('toVertice %s is invalid!' % str(toVertice))
    self.save(**edgeArgs)