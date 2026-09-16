def search_databases(self, search_term, location=None, markets_only=False,
    databases_to_search=None, allow_internal=False):
    dict_list = []
    if allow_internal:
        internal_dict = {}
        for k, v in self.database['items'].items():
            if v.get('lcopt_type') == 'intermediate':
                internal_dict[k] = v
        dict_list.append(internal_dict)
    if databases_to_search is None:
        dict_list += [x['items'] for x in self.external_databases]
    else:
        dict_list += [x['items'] for x in self.external_databases if x[
            'name'] in databases_to_search]
    data = Dictionaries(*dict_list)
    query = Query()
    if markets_only:
        market_filter = Filter('name', 'has', 'market for')
        query.add(market_filter)
    if location is not None:
        location_filter = Filter('location', 'is', location)
        query.add(location_filter)
    query.add(Filter('name', 'ihas', search_term))
    result = query(data)
    return result