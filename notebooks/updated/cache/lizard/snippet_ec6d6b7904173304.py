def update(self, pop: Union[pd.DataFrame, pd.Series]):
    if not pop.empty:
        if isinstance(pop, pd.Series):
            if pop.name in self._columns:
                affected_columns = [pop.name]
            elif len(self._columns) == 1:
                affected_columns = self._columns
            else:
                raise PopulationError(
                    'Cannot update with a Series unless the series name equals a column name or there is only a single column in the view'
                    )
        else:
            affected_columns = set(pop.columns)
        affected_columns = set(affected_columns).intersection(self._columns)
        state_table = self.manager.get_population(True)
        if not self.manager.growing:
            affected_columns = set(affected_columns).intersection(state_table
                .columns)
        for c in affected_columns:
            if c in state_table:
                v = state_table[c].values
                if isinstance(pop, pd.Series):
                    v2 = pop.values
                else:
                    v2 = pop[c].values
                v[pop.index] = v2
                if v.dtype != v2.dtype:
                    if not self.manager.growing:
                        raise PopulationError(
                            'Component corrupting population table. Old column type: {} New column type: {}'
                            .format(v.dtype, v2.dtype))
                    v = v.astype(v2.dtype)
            elif isinstance(pop, pd.Series):
                v = pop.values
            else:
                v = pop[c].values
            self.manager._population[c] = v