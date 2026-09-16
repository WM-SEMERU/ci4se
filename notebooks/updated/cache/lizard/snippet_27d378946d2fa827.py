def match_relations(self, el, relation):
    found = False
    if relation[0].rel_type.startswith(':'):
        found = self.match_future_relations(el, relation)
    else:
        found = self.match_past_relations(el, relation)
    return found