def p_expression_invar(self, p):
    _LOGGER.debug('expresion -> expresion IN VAR')
    if p[3] not in self._VAR_VALUES:
        if self._autodefine_vars:
            self._VAR_VALUES[p[3]] = TypedList([])
        else:
            raise TypeError('list expected for IN operator')
    l = self._VAR_VALUES[p[3]]
    if l.type != TypedList.LIST:
        raise TypeError('list expected for IN operator')
    p[3] = l
    self.p_expression_inlist(p)