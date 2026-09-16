def where_has(self, relation, extra, operator='>=', count=1):
    return self.has(relation, operator, count, 'and', extra)