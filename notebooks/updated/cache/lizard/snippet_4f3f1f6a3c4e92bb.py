def journal_composition(collection, issn, raw=False):
    tc = ThriftClient()
    body = {'query': {'filtered': {}}}
    fltr = {}
    query = {'query': {'bool': {'must': [{'match': {'collection':
        collection}}, {'match': {'issn': issn}}]}}}
    body['query']['filtered'].update(fltr)
    body['query']['filtered'].update(query)
    query_parameters = [('size', '0'), ('search_type', 'count')]
    body['aggs'] = {'issues': {'cardinality': {'field': 'issue'}},
        'citations': {'sum': {'field': 'citations'}}, 'citable': {'filter':
        {'terms': {'document_type': [i for i in utils.
        CITABLE_DOCUMENT_TYPES]}}}}
    query_result = tc.search('article', json.dumps(body), query_parameters)
    computed = _compute_journal_composition(query_result)
    return query_result if raw else computed