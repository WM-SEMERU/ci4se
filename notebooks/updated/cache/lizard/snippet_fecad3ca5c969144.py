def initialize(self, pid, ore_software_id=d1_common.const.ORE_SOFTWARE_ID):
    for k in list(d1_common.const.ORE_NAMESPACE_DICT.keys()):
        self.bind(k, d1_common.const.ORE_NAMESPACE_DICT[k])
    oid = self._pid_to_id(pid)
    ore = rdflib.URIRef(oid)
    self.add((ore, rdflib.RDF.type, ORE.ResourceMap))
    self.add((ore, DCTERMS.identifier, rdflib.term.Literal(pid)))
    self.add((ore, DCTERMS.creator, rdflib.term.Literal(ore_software_id)))
    ag = rdflib.URIRef(oid + '#aggregation')
    self.add((ore, ORE.describes, ag))
    self.add((ag, rdflib.RDF.type, ORE.Aggregation))
    self.add((ORE.Aggregation, rdflib.RDFS.isDefinedBy, ORE.term('')))
    self.add((ORE.Aggregation, rdflib.RDFS.label, rdflib.term.Literal(
        'Aggregation')))
    self._ore_initialized = True