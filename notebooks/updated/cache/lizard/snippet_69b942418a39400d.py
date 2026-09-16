def NegateQueryFilter(es_query):
    query = es_query.to_dict().get('query', {})
    filtered = query.get('filtered', {})
    negated_filter = filtered.get('filter', {})
    return Not(**negated_filter)