def get_full_dependents(self, term_id, relations, counter=0):
    counter += 1
    deps = self.relations_for_term
    if term_id in deps and len(deps.get(term_id)) > 0:
        for dep in deps.get(term_id):
            if not dep[1] in relations:
                relations.append(dep[1])
                if dep[1] in deps:
                    deprelations = self.get_full_dependents(dep[1],
                        relations, counter)
                    for deprel in deprelations:
                        if not deprel in relations:
                            relations.append(deprel)
    return relations