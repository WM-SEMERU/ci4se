def apply_trend_constraint(self, limit, dt, **kwargs):
    if 'RV monitoring' not in self.constraints:
        self.constraints.append('RV monitoring')
    for pop in self.poplist:
        if not hasattr(pop, 'dRV'):
            continue
        pop.apply_trend_constraint(limit, dt, **kwargs)
    self.trend_limit = limit
    self.trend_dt = dt