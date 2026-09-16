def _relation_exists(self, connection, relation):
    query = (
        "SELECT 1 FROM sqlite_master WHERE (type='table' OR type='view') AND name=?;"
        )
    cursor = connection.cursor()
    cursor.execute(query, [relation])
    result = cursor.fetchall()
    return result == [(1,)]