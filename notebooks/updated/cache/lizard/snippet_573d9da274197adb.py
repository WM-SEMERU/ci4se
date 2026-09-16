def standardized_compound(self):
    for c in self.record['compound']:
        if c['id']['type'] == CompoundIdType.STANDARDIZED:
            return Compound.from_cid(c['id']['id']['cid'])