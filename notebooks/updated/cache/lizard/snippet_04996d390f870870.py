def unregister(self, document):
    if document not in self.documents.keys():
        self.log.warning('Can not unregister document %s' % document)
    else:
        del self.documents[document]
        self.__log.debug('Document %s got unregistered' % document)