def print_summary(self):
    if self.sources_valid:
        printDebug('----------\nLoaded %d triples.\n----------' % len(self.
            rdflib_graph), fg='white')
        printDebug('RDF sources loaded successfully: %d of %d.' % (len(self
            .sources_valid), len(self.sources_valid) + len(self.
            sources_invalid)), fg='green')
        for s in self.sources_valid:
            printDebug("..... '" + s + "'", fg='white')
        printDebug('----------', fg='white')
    else:
        printDebug('Sorry - no valid RDF was found', fg='red')
    if self.sources_invalid:
        printDebug(
            '----------\nRDF sources failed to load: %d.\n----------' % len
            (self.sources_invalid), fg='red')
        for s in self.sources_invalid:
            printDebug('-> ' + s, fg='red')