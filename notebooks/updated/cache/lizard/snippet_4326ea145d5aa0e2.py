def get_database_tag(self):

    def parse_response(doc):
        self._database_tag = doc['tag']
        return self._database_tag

    def create_new(fail):
        fail.trap(NotFoundError)
        doc = {'_id': doc_id, 'tag': unicode(uuid.uuid1())}
        return self.save_document(doc)

    def conflict_handler(fail):
        fail.trap(ConflictError)
        return self.get_database_tag()
    if not hasattr(self, '_database_tag'):
        doc_id = '_local/database_tag'
        d = self.get_document(doc_id)
        d.addErrback(create_new)
        d.addErrback(conflict_handler)
        d.addCallback(parse_response)
        return d
    else:
        return defer.succeed(self._database_tag)