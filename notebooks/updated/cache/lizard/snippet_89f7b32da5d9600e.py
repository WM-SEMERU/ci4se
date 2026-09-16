def search(self, **kw):
    q = db.select(self.table).condition('status', 'active')
    for k, v in kw:
        q.condition(k, v)
    data = q.execute()
    users = []
    for user in data:
        users.append(self.load(user, self.model))
    return users