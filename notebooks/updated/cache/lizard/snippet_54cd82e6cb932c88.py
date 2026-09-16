def get_namespace_reveal(self, namespace_id, include_history=True):
    cur = self.db.cursor()
    namespace_reveal = namedb_get_namespace_reveal(cur, namespace_id, self.
        lastblock, include_history=include_history)
    return namespace_reveal