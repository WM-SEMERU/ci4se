def update(self, id, data):
    self.db.execute(['UPDATE comments SET', ','.join(key + '=' + '?' for
        key in data), 'WHERE id=?;'], list(data.values()) + [id])
    return self.get(id)