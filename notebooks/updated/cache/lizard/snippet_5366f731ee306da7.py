def exists(self, document_or_id=None, session=None, **kwargs):
    if kwargs:
        f = self.__files.find_one(kwargs, ['_id'], session=session)
    else:
        f = self.__files.find_one(document_or_id, ['_id'], session=session)
    return f is not None