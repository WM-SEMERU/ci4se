def sentiment(self):
    if self._sentiment is None:
        self._sentiment = int(self._element.get('sentiment'))
    return self._sentiment