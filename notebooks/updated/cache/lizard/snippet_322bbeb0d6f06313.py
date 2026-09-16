def scan(self, index, doc_type, query=None, scroll='5m', preserve_order=
    False, size=10, **kwargs):
    if not preserve_order:
        kwargs['search_type'] = 'scan'
    results = yield self.search(index=index, doc_type=doc_type, body=query,
        size=size, scroll=scroll, **kwargs)
    returnValue(Scroller(self, results, scroll, size))