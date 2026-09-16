def get_by_id(self, id, change_notes=False):
    graph = uri_to_graph('%s/%s.rdf' % (self.url, id), session=self.session)
    if graph is False:
        log.debug('Failed to retrieve data for %s/%s.rdf' % (self.url, id))
        return False
    things = things_from_graph(graph, self.subclasses, self.concept_scheme)
    if len(things) == 0:
        return False
    c = things[0]
    return c