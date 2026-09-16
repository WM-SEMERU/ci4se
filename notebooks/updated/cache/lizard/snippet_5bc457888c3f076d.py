def get_parents(self, uri, type='all'):
    all_parents = set(self.isa_or_partof_closure.get(uri, []))
    if not all_parents or type == 'all':
        return all_parents
    if type == 'immediate':
        node = rdflib.term.URIRef(uri)
        immediate_parents = list(set(self.isa_or_partof_objects(node)))
        return [p.toPython() for p in immediate_parents]
    elif type == 'top':
        top_parents = [p for p in all_parents if not self.
            isa_or_partof_closure.get(p)]
        return top_parents