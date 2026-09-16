def _facet_counts(items):
    facets = {}
    for name, data in items:
        facets[name] = FacetResult(name, data)
    return facets