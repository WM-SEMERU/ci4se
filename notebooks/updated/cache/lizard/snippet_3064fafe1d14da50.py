def pid(self):
    return hashlib.md5(':'.join([self.__class__.__name__, self._uri]).
        encode('utf-8')).hexdigest()