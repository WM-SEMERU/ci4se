def _has_nested(self, relations, operator='>=', count=1, boolean='and',
    extra=None):
    relations = relations.split('.')

    def closure(q):
        if len(relations) > 1:
            q.where_has(relations.pop(0), closure)
        else:
            q.has(relations.pop(0), operator, count, boolean, extra)
    return self.where_has(relations.pop(0), closure)