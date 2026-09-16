def index(self, record):
    index, doc_type = self.record_to_index(record)
    return self.client.index(id=str(record.id), version=record.revision_id,
        version_type=self._version_type, index=index, doc_type=doc_type,
        body=self._prepare_record(record, index, doc_type))