def get(self, file_id):

    def ok(doc):
        if doc is None:
            raise NoFile('TxMongo: no file in gridfs with _id {0}'.format(
                repr(file_id)))
        return GridOut(self.__collection, doc)
    return self.__collection.files.find_one({'_id': file_id}).addCallback(ok)