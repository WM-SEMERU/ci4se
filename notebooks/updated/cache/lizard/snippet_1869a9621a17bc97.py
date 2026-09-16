def _marshal_claims(self, query_claims):
    claims = reduce_claims(query_claims)
    self.data['claims'] = claims
    entities = set()
    for eid in claims:
        if self.user_labels:
            if eid in self.user_labels or eid == 'P31':
                entities.add(eid)
            else:
                continue
        else:
            entities.add(eid)
        for val in claims[eid]:
            if utils.is_text(val) and re.match('^Q\\d+$', val):
                entities.add(val)
    self.data['entities'] = list(entities)