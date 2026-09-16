def graphiter(self, graph, target, ascendants=0, descendants=1):
    asc = 0 + ascendants
    if asc != 0:
        asc -= 1
    desc = 0 + descendants
    if desc != 0:
        desc -= 1
    t = str(target)
    if descendants != 0 and self.downwards[t] is True:
        self.downwards[t] = False
        for pred, obj in graph.predicate_objects(target):
            if desc == 0 and isinstance(obj, BNode):
                continue
            self.add((target, pred, obj))
            if desc != 0 and self.downwards[str(obj)] is True:
                self.graphiter(graph, target=obj, ascendants=0, descendants
                    =desc)
    if ascendants != 0 and self.updwards[t] is True:
        self.updwards[t] = False
        for s, p in graph.subject_predicates(object=target):
            if desc == 0 and isinstance(s, BNode):
                continue
            self.add((s, p, target))
            if asc != 0 and self.updwards[str(s)] is True:
                self.graphiter(graph, target=s, ascendants=asc, descendants=0)