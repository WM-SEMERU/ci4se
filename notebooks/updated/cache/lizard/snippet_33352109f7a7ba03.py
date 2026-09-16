def search_tweets_iterable(self, order, callback=None):
    if callback:
        if not callable(callback):
            raise TwitterSearchException(1018)
        self.__callback = callback
    self.search_tweets(order)
    return self