def _pickUpIteration(self, searchAnchor, objectsToSkip):
    self._searchAnchor = searchAnchor
    self._distanceFromAnchor = objectsToSkip
    self._searchIterator = self._search(searchAnchor, self._request.end if 
        self._request.end != 0 else None)
    obj = next(self._searchIterator)
    if searchAnchor == self._request.start:
        for _ in range(objectsToSkip):
            obj = next(self._searchIterator)
    else:
        while self._getStart(obj) < searchAnchor:
            obj = next(self._searchIterator)
        for _ in range(objectsToSkip):
            if self._getStart(obj) != searchAnchor:
                raise exceptions.BadPageTokenException
            obj = next(self._searchIterator)
    self._currentObject = obj
    self._nextObject = next(self._searchIterator, None)