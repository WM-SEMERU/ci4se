def _delete_action(self, payload):
    index, doc_type = payload.get('index'), payload.get('doc_type')
    if not (index and doc_type):
        record = Record.get_record(payload['id'])
        index, doc_type = self.record_to_index(record)
    return {'_op_type': 'delete', '_index': index, '_type': doc_type, '_id':
        payload['id']}