def _build(self, constraint_spec):
    self._sections = []
    for sval in constraint_spec:
        rpt_fld = self._base_report_fields.copy()
        if self._is_python(sval.constraints):
            query, proj = self._process_python(sval.constraints)
            rpt_fld.update(proj.to_mongo())
        else:
            query = MongoQuery()
            if sval.constraints is not None:
                groups = self._process_constraint_expressions(sval.constraints)
                projection = Projection()
                for cg in groups.values():
                    for c in cg:
                        projection.add(c.field, c.op, c.value)
                        query.add_clause(MongoClause(c))
                    if self._add_exists:
                        for c in cg.existence_constraints:
                            query.add_clause(MongoClause(c, exists_main=True))
                rpt_fld.update(projection.to_mongo())
        cond_query = MongoQuery()
        if sval.filters is not None:
            cond_groups = self._process_constraint_expressions(sval.filters,
                rev=False)
            for cg in cond_groups.values():
                for c in cg:
                    cond_query.add_clause(MongoClause(c, rev=False))
        result = self.SectionParts(cond_query, query, sval.sampler, rpt_fld)
        self._sections.append(result)