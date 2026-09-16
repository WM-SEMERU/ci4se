def push(self):
    self._refresh_connection()
    if not self._mapping_created:
        logger.debug("Pushing mapping for Elasticsearch index '%s'.", self.
            __class__.__name__)
        self.create_mapping()
    if not self.push_queue:
        logger.debug('No documents to push, skipping push.')
        return
    logger.debug('Found %s documents to push to Elasticsearch.', len(self.
        push_queue))
    bulk(connections.get_connection(), (doc.to_dict(True) for doc in self.
        push_queue), refresh=True)
    self.push_queue = []
    logger.debug('Finished pushing builded documents to Elasticsearch server.')