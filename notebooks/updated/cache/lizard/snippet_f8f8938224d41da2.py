def txn_getAssociation(self, server_url, handle=None):
    if handle is not None:
        self.db_get_assoc(server_url, handle)
    else:
        self.db_get_assocs(server_url)
    rows = self.cur.fetchall()
    if len(rows) == 0:
        return None
    else:
        associations = []
        for values in rows:
            values = list(values)
            values[1] = self.blobDecode(values[1])
            assoc = Association(*values)
            if assoc.expiresIn == 0:
                self.txn_removeAssociation(server_url, assoc.handle)
            else:
                associations.append((assoc.issued, assoc))
        if associations:
            associations.sort()
            return associations[-1][1]
        else:
            return None