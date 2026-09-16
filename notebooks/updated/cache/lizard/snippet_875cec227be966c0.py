def AddAsMessage(self, rdfvalue_in, source, mutation_pool=None):
    self.Add(rdf_flows.GrrMessage(payload=rdfvalue_in, source=source),
        mutation_pool=mutation_pool)