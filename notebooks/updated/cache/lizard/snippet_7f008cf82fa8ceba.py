def read(self):
    cursor = self.get_collection().find({'_id': {'$in': self._document_ids},
        self._field: {'$exists': True}}, {self._field: True})
    return {doc['_id']: doc[self._field] for doc in cursor}