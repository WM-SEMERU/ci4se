def update_dbxref(self, feature_id, old_db, old_accession, new_db,
    new_accession, organism=None, sequence=None):
    data = {'features': [{'uniquename': feature_id, 'old_dbxrefs': [{'db':
        old_db, 'accession': old_accession}], 'new_dbxrefs': [{'db': new_db,
        'accession': new_accession}]}]}
    data = self._update_data(data, organism, sequence)
    return self.post('deleteDbxref', data)