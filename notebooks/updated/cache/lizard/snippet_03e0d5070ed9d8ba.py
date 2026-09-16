def get_sampletypes(self):
    query = {'portal_type': 'SampleType', 'sort_on': 'sortable_title',
        'sort_order': 'ascending', 'is_active': True}
    results = api.search(query, 'bika_setup_catalog')
    return map(api.get_object, results)