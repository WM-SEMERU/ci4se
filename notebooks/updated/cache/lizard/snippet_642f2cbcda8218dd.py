def list_relations(self):
    for node in self.iter_nodes():
        for relation, target in self.relations_of(node.obj, True):
            yield node.obj, relation, target