def delete(self, entry):
    c = self.conn.cursor()
    c.execute('DELETE FROM oath WHERE key = ?', (entry.data['key'],))