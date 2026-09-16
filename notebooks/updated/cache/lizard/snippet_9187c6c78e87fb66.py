def _GenConfig(self, cfg):
    merged = self.default.copy()
    for setting, vals in iteritems(cfg):
        option, operator = (setting.split(None, 1) + [None])[:2]
        vals = set(vals)
        default = set(self.default.get(option, []))
        if operator == '+':
            vals = default.union(vals)
        elif operator == '-':
            vals = default.difference(vals)
        merged[option] = list(vals)
    return rdf_protodict.AttributedDict(**merged)