def populateFromFile(self, dataUrl):
    self._dbFilePath = dataUrl
    self._rdfGraph = rdflib.ConjunctiveGraph()
    self._dataUrl = dataUrl
    self._scanDataFiles(self._dataUrl, ['*.ttl'])
    cgdTTL = rdflib.URIRef('http://data.monarchinitiative.org/ttl/cgd.ttl')
    versionInfo = rdflib.URIRef('http://www.w3.org/2002/07/owl#versionInfo')
    self._version = None
    for _, _, obj in self._rdfGraph.triples((cgdTTL, versionInfo, None)):
        self._version = obj.toPython()
    self._initializeLocationCache()