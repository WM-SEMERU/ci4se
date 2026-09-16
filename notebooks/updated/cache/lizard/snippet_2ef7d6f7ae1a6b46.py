def add_term_facet(self, *args, **kwargs):
    self.facets.append(TermFacet(*args, **kwargs))