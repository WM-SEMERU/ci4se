def list_topics(self, Nwords=10):
    return [(k, self.list_topic(k, Nwords)) for k in xrange(len(self.phi))]