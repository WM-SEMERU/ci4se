def get_block(self, namespace, offset, key):
    cursor = self.cursor
    cursor.execute(
        'SELECT data, flags FROM gauged_data WHERE namespace = %s AND "offset" = %s AND key = %s'
        , (namespace, offset, key))
    row = cursor.fetchone()
    return (None, None) if row is None else row