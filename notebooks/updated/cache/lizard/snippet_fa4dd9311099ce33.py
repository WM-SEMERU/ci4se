def from_where(cls, where):
    if where.conjunction:
        return Conjunction.from_clause(where)
    else:
        return cls.from_clause(where[0])