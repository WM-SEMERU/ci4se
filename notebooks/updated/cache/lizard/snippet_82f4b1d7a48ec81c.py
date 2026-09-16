def get_by_id(self, id):
    with contextlib.closing(self.database.cursor()) as cursor:
        cursor.execute('SELECT id, name FROM users WHERE id=?', (id,))
        return cursor.fetchone()