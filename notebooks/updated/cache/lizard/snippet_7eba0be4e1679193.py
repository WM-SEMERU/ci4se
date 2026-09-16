def ReadAllArtifacts(self, cursor=None):
    cursor.execute('SELECT definition FROM artifacts')
    return [_RowToArtifact(row) for row in cursor.fetchall()]