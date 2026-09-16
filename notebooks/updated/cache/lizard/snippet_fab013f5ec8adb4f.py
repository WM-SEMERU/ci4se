def delete(self, id):
    refs = self.db.execute('SELECT * FROM comments WHERE parent=?', (id,)
        ).fetchone()
    if refs is None:
        self.db.execute('DELETE FROM comments WHERE id=?', (id,))
        self._remove_stale()
        return None
    self.db.execute('UPDATE comments SET text=? WHERE id=?', ('', id))
    self.db.execute('UPDATE comments SET mode=? WHERE id=?', (4, id))
    for field in ('author', 'website'):
        self.db.execute('UPDATE comments SET %s=? WHERE id=?' % field, (
            None, id))
    self._remove_stale()
    return self.get(id)