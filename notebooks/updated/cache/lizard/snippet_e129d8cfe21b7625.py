def ensure_hist_size(self):
    if self.marker_index_hist_size == 0:
        return
    result = self.es.search(index=self.marker_index, doc_type=self.
        marker_doc_type, body={'query': {'term': {'target_index': self.
        index}}}, sort=('date:desc',))
    for i, hit in enumerate(result.get('hits').get('hits'), start=1):
        if i > self.marker_index_hist_size:
            marker_document_id = hit.get('_id')
            self.es.delete(id=marker_document_id, index=self.marker_index,
                doc_type=self.marker_doc_type)
    self.es.indices.flush(index=self.marker_index)