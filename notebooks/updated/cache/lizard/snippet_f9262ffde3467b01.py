def _match(self, doc, where):
    assert isinstance(where, dict), 'where is not a dictionary'
    assert isinstance(doc, dict), 'doc is not a dictionary'
    try:
        return all([(doc[k] == v) for k, v in where.items()])
    except KeyError:
        return False