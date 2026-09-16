def is_user_valid(self, userID):
    cur = self.conn.cursor()
    cur.execute('SELECT * FROM users WHERE id=? LIMIT 1', [userID])
    results = cur.fetchall()
    cur.close()
    return len(results) > 0