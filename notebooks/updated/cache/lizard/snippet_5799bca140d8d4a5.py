def make_model(self, *args, **kwargs):
    for stmt in self.statements:
        if isinstance(stmt, RegulateActivity):
            self._add_regulate_activity(stmt)
        elif isinstance(stmt, RegulateAmount):
            self._add_regulate_amount(stmt)
        elif isinstance(stmt, Modification):
            self._add_modification(stmt)
        elif isinstance(stmt, SelfModification):
            self._add_selfmodification(stmt)
        elif isinstance(stmt, Gef):
            self._add_gef(stmt)
        elif isinstance(stmt, Gap):
            self._add_gap(stmt)
        elif isinstance(stmt, Complex):
            self._add_complex(stmt)
        else:
            logger.warning('Unhandled statement type: %s' % stmt.__class__.
                __name__)
    if kwargs.get('grouping'):
        self._group_nodes()
        self._group_edges()
    return self.print_cyjs_graph()