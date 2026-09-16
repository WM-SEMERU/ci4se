def _minimize_joins(self):
    joins_group = []
    for join in self._joins:
        append_new = True
        for join_group in joins_group:
            if join_group[0]['table'] == join['table'] and join_group[0]['ons'
                ] == join['ons']:
                join_group.append(join)
                append_new = False
                break
        if append_new:
            joins_group.append([join])
    self._joins = []
    for joins in joins_group:
        if len(joins) > 1 and any(bool(join['type'] == INNER_JOIN) for join in
            joins):
            joins[0]['type'] = INNER_JOIN
            self._joins.append(joins[0])
        elif len(joins) > 1 and all(join['type'] == joins[0]['type'] for
            join in joins):
            self._joins.append(joins[0])
        else:
            self._joins.extend(joins)