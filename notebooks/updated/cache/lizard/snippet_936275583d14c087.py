def process(self, pre_search_condition=None, **kwargs):
    records = self.query_by_args(pre_search_condition=pre_search_condition,
        **kwargs)
    serializer = self.serializer(records['items'], many=True)
    result = {'data': serializer.data, 'draw': records['draw'],
        'recordsTotal': records['total'], 'recordsFiltered': records['count']}
    return result