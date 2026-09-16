def search(self, name: str=None, acc_type: str=None):
    query = self.query
    if name is not None:
        query = query.filter(Account.name == name)
    if acc_type is not None:
        acc_type = acc_type.upper()
        query = query.filter(Account.type == acc_type)
    return query.all()