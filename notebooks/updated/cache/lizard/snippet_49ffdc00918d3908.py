def _formatOntologyTermObject(self, terms, element_type):
    elementClause = None
    if not isinstance(terms, collections.Iterable):
        terms = [terms]
    elements = []
    for term in terms:
        if term.term_id:
            elements.append('?{} = <{}> '.format(element_type, term.term_id))
        else:
            elements.append('?{} = <{}> '.format(element_type, self.
                _toNamespaceURL(term.term)))
    elementClause = '({})'.format(' || '.join(elements))
    return elementClause