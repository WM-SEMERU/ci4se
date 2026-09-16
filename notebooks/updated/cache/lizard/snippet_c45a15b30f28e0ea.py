def remove(self, obj, commit=True):
    database = self._database(writable=True)
    database.delete_document(TERM_PREFIXES[ID] + get_identifier(obj))
    database.close()