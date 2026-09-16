def makeStylesheetResource(self, path, registry):
    return StylesheetRewritingResourceWrapper(File(path), self.
        installedOfferingNames, self.rootURL)