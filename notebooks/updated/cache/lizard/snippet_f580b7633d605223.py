def apply_queryset_rules(self, qs):
    clauses = {'filter': [], 'exclude': []}
    for rule in self.drip_model.queryset_rules.all():
        clause = clauses.get(rule.method_type, clauses['filter'])
        kwargs = rule.filter_kwargs(qs, now=self.now)
        clause.append(Q(**kwargs))
        qs = rule.apply_any_annotation(qs)
    if clauses['exclude']:
        qs = qs.exclude(functools.reduce(operator.or_, clauses['exclude']))
    qs = qs.filter(*clauses['filter'])
    return qs