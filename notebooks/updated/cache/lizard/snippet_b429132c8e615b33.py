def iterconnections(self):
    return itertools.chain(self.secureConnectionCache.cachedConnections.
        itervalues(), iter(self.subConnections), (self.dispatcher or ()) and
        self.dispatcher.iterconnections())