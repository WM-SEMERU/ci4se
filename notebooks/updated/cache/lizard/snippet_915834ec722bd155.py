def _query(self, action, qobj):
    if action == 'labels':
        return qobj.labels(self._pop_entities())
    elif action == 'wikidata':
        return qobj.wikidata(self.params.get('title'), self.params.get(
            'wikibase'))