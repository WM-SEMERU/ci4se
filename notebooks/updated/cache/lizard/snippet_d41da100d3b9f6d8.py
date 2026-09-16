def collection_names(self, _deadline=None):

    def ok(results):
        names = [r['name'] for r in results]
        names = [n[len(str(self)) + 1:] for n in names if n.startswith(str(
            self) + '.')]
        names = [n for n in names if '$' not in n]
        return names
    return self['system.namespaces'].find(_deadline=_deadline).addCallback(ok)