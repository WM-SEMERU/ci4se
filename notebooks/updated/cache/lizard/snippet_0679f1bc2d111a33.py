def get_items_by_search(self, item_query, item_search):
    and_list = list()
    or_list = list()
    for term in item_query._query_terms:
        and_list.append({term: item_query._query_terms[term]})
    for term in item_query._keyword_terms:
        or_list.append({term: item_query._keyword_terms[term]})
    if item_search._id_list is not None:
        identifiers = [ObjectId(i.identifier) for i in item_search._id_list]
        and_list.append({'_id': {'$in': identifiers}})
    if or_list:
        and_list.append({'$or': or_list})
    view_filter = self._view_filter()
    if view_filter:
        and_list.append(view_filter)
    if and_list:
        query_terms = {'$and': and_list}
    collection = JSONClientValidated('assessment', collection='Item',
        runtime=self._runtime)
    if item_search.start is not None and item_search.end is not None:
        result = collection.find(query_terms)[item_search.start:item_search.end
            ]
    else:
        result = collection.find(query_terms)
    return searches.ItemSearchResults(result, dict(item_query._query_terms),
        runtime=self._runtime)