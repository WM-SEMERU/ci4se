def match(cls, field, query, operator=None):
    instance = cls(match={field: {'query': query}})
    if operator is not None:
        instance['match'][field]['operator'] = operator
    return instance