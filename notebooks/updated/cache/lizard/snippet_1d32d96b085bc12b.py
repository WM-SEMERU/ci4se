def note_delete(self, note_id):
    return self._get('notes/{0}.json'.format(note_id), method='DELETE',
        auth=True)