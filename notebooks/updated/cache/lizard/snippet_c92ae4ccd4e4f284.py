def spo_search(self, subject=None, predicate=None, object=None):
    spo_query = '%s %s %s' % (self.spoencode(subject), self.spoencode(
        predicate), self.spoencode(object))
    return self.find_statements(spo_query)