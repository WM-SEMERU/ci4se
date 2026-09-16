def removeSpecfile(self, specfiles):
    for specfile in aux.toList(specfiles):
        del self.container[specfile]
        del self.info[specfile]