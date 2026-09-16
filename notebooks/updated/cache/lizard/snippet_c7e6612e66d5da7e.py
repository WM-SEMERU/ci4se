def bm25(dataset, query, k1=1.5, b=0.75):
    if type(dataset) != _turicreate.SArray:
        raise TypeError(
            'bm25 requires an SArray of dict, list, or str type' +
            ', where each dictionary whose keys are words and whose values' +
            ' are word frequency.')
    sf = _SFrame({'docs': dataset})
    if type(query) is dict:
        query = list(query.keys())
    if type(query) is _turicreate.SArray:
        query = list(query)
    if type(query) is set:
        query = list(query)
    if type(query) is not list:
        raise TypeError('The query must either be an SArray of str type, ' +
            ' a list of strings, or a set of strings.')
    sf = sf.add_row_number('doc_id')
    sf = sf.dropna('docs')
    scores = _feature_engineering.BM25('docs', query, k1, b,
        output_column_name='bm25').fit_transform(sf)
    if scores['docs'].dtype is dict:
        scores['doc_terms'] = scores['docs'].dict_keys()
    elif scores['docs'].dtype is list:
        scores['doc_terms'] = scores['docs'].apply(lambda x: list(set(x)))
    elif scores['docs'].dtype is str:
        scores['doc_terms'] = count_words(scores['docs']).dict_keys()
    else:
        raise TypeError('bm25 requires an SArray of dict, list, or str type')
    scores['doc_counts'] = scores['doc_terms'].apply(lambda x: len([word for
        word in query if word in x]))
    scores = scores[scores['doc_counts'] > 0]
    scores = scores.select_columns(['doc_id', 'bm25'])
    return scores