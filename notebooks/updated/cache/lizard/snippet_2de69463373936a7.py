def ReadArtifact(self, name, cursor=None):
    cursor.execute('SELECT definition FROM artifacts WHERE name = %s', [name])
    row = cursor.fetchone()
    if row is None:
        raise db.UnknownArtifactError(name)
    else:
        return _RowToArtifact(row)