def do_next(self, line):
    if not self.current:
        print(
            "Please select an ontology first. E.g. use the 'ls ontologies' or 'get ontology <name>' commands."
            )
    elif self.currentEntity:
        g = self.current['graph']
        if self.currentEntity['type'] == 'class':
            nextentity = g.nextClass(self.currentEntity['object'].uri)
            self._select_class(str(nextentity.uri))
        elif self.currentEntity['type'] == 'property':
            nextentity = g.nextProperty(self.currentEntity['object'].uri)
            self._select_property(str(nextentity.uri))
        elif self.currentEntity['type'] == 'concept':
            nextentity = g.nextConcept(self.currentEntity['object'].uri)
            self._select_concept(str(nextentity.uri))
        else:
            print('Not implemented')
    elif len(self.all_ontologies) > 1:
        nextonto = self._next_ontology()
        self._load_ontology(nextonto)
    else:
        self._print('Only one ontology available in repository.')