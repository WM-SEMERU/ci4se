def _setdefault(self, relation):
    self.add_schema(relation.database, relation.schema)
    key = relation.key()
    return self.relations.setdefault(key, relation)