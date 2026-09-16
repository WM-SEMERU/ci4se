def vars(self, exclude_where=False, exclude_select=False):

    def edges_get_all_vars(e):
        output = set()
        if is_text(e.value):
            output.add(e.value)
        if is_expression(e.value):
            output |= e.value.vars()
        if e.domain.key:
            output.add(e.domain.key)
        if e.domain.where:
            output |= e.domain.where.vars()
        if e.range:
            output |= e.range.min.vars()
            output |= e.range.max.vars()
        if e.domain.partitions:
            for p in e.domain.partitions:
                if p.where:
                    output |= p.where.vars()
        return output
    output = set()
    try:
        output |= self.frum.vars()
    except Exception:
        pass
    if not exclude_select:
        for s in listwrap(self.select):
            output |= s.value.vars()
    for s in listwrap(self.edges):
        output |= edges_get_all_vars(s)
    for s in listwrap(self.groupby):
        output |= edges_get_all_vars(s)
    if not exclude_where:
        output |= self.where.vars()
    for s in listwrap(self.sort):
        output |= s.value.vars()
    try:
        output |= UNION(e.vars() for e in self.window)
    except Exception:
        pass
    return output