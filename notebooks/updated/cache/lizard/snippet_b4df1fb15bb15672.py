def get_objects(self, subject=None, predicate=None):
    results = self.rdf.objects(subject, predicate)
    return list(results)