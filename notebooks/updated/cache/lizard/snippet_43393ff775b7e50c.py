def txn_removeAssociation(self, server_url, handle):
    self.db_remove_assoc(server_url, handle)
    return self.cur.rowcount > 0