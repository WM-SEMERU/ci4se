def as_dict(self, replace_value_names=True):
    r = RootSectionTerm(doc=self)
    for s in self:
        for t in s:
            r.terms.append(t)
    return r.as_dict(replace_value_names)