def _flatten_ancestors(self, include_part_of=True):

    def get_all_ancestors(term):
        ancestors = set()
        for id_ in term.is_a:
            ancestors.add(id_)
            ancestors.update(get_all_ancestors(self.terms[id_]))
        if include_part_of:
            for id_ in term.part_of:
                ancestors.add(id_)
                ancestors.update(get_all_ancestors(self.terms[id_]))
        return ancestors
    for term in self.terms.values():
        term.ancestors = get_all_ancestors(term)