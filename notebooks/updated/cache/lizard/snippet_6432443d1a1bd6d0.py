def in_(self, qfield, *values):
    qfield = resolve_name(self.type, qfield)
    self.filter(QueryExpression({qfield: {'$in': [qfield.wrap_value(value) for
        value in values]}}))
    return self