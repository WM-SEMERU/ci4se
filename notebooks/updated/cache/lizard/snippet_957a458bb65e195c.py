def _normalize_json_search_response(self, json):
    result = {}
    if 'facet_counts' in json:
        result['facet_counts'] = json['facet_counts']
    if 'grouped' in json:
        result['grouped'] = json['grouped']
    if 'stats' in json:
        result['stats'] = json['stats']
    if 'response' in json:
        result['num_found'] = json['response']['numFound']
        result['max_score'] = float(json['response']['maxScore'])
        docs = []
        for doc in json['response']['docs']:
            resdoc = {}
            if '_yz_rk' in doc:
                resdoc = doc
            else:
                resdoc['id'] = doc['id']
                if 'fields' in doc:
                    for k, v in six.iteritems(doc['fields']):
                        resdoc[k] = v
            docs.append(resdoc)
        result['docs'] = docs
    return result