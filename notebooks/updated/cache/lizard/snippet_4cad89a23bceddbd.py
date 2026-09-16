def put(self, pid, record, **kwargs):
    if request.mimetype not in self.loaders:
        raise UnsupportedMediaRESTError(request.mimetype)
    data = self.loaders[request.mimetype]()
    if data is None:
        raise InvalidDataRESTError()
    self.check_etag(str(record.revision_id))
    record.clear()
    record.update(data)
    record.commit()
    db.session.commit()
    if self.indexer_class:
        self.indexer_class().index(record)
    return self.make_response(pid, record, links_factory=self.links_factory)