def index(self, refresh=False):
    es = connections.get_connection('default')
    index = self.__class__.search_objects.mapping.index
    doc_type = self.__class__.search_objects.mapping.doc_type
    es.index(index, doc_type, id=self.pk, body=self.to_dict(), refresh=refresh)