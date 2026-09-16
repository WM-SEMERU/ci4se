def extract(self, searches, tree=None, as_dict=True):
    if self.tree is None or self.pq is None:
        self.load()
    if tree is None:
        pq = self.pq
    else:
        pq = PyQuery(tree, css_translator=PDFQueryTranslator())
    results = []
    formatter = None
    parent = pq
    for search in searches:
        if len(search) < 3:
            search = list(search) + [formatter]
        key, search, tmp_formatter = search
        if key == 'with_formatter':
            if isinstance(search, six.string_types):
                formatter = lambda o, search=search: getattr(o, search)()
            elif hasattr(search, '__call__') or not search:
                formatter = search
            else:
                raise TypeError(
                    'Formatter should be either a pyquery method name or a callable function.'
                    )
        elif key == 'with_parent':
            parent = pq(search) if search else pq
        else:
            try:
                result = parent('*').filter(search) if hasattr(search,
                    '__call__') else parent(search)
            except cssselect.SelectorSyntaxError as e:
                raise cssselect.SelectorSyntaxError(
                    "Error applying selector '%s': %s" % (search, e))
            if tmp_formatter:
                result = tmp_formatter(result)
            results += result if type(result) == tuple else [[key, result]]
    if as_dict:
        results = dict(results)
    return results