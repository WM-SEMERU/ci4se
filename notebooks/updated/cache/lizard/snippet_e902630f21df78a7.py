def get_raw_query(self):
    query = self.base_query.copy()
    search_query = self.search_query.copy()
    query.update(search_query)
    sorting = self.resolve_sorting(query)
    query.update(sorting)
    catalog = api.get_tool(self.catalog_name)
    sort_on = query.get('sort_on', None)
    if sort_on and not self.is_sortable_index(sort_on, catalog):
        del query['sort_on']
    return query