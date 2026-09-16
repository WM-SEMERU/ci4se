def addComponentToPathway(self, component_id, pathway_id):
    self.graph.addTriple(component_id, self.globaltt['involved in'], pathway_id
        )
    return