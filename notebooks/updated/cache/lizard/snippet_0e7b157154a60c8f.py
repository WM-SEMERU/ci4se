def timeseries(self):
    if self._timeseries is None:
        if isinstance(self.grid, MVGrid):
            voltage_level = 'mv'
        elif isinstance(self.grid, LVGrid):
            voltage_level = 'lv'
        ts_total = None
        for sector in self.consumption.keys():
            consumption = self.consumption[sector]
            try:
                ts = self.grid.network.timeseries.load[sector, voltage_level
                    ].to_frame('p')
            except KeyError:
                try:
                    ts = self.grid.network.timeseries.load[sector].to_frame('p'
                        )
                except KeyError:
                    logger.exception('No timeseries for load of type {} given.'
                        .format(sector))
                    raise
            ts = ts * consumption
            ts_q = self.timeseries_reactive
            if ts_q is not None:
                ts['q'] = ts_q.q
            else:
                ts['q'] = ts['p'] * self.q_sign * tan(acos(self.power_factor))
            if ts_total is None:
                ts_total = ts
            else:
                ts_total.p += ts.p
                ts_total.q += ts.q
        return ts_total
    else:
        return self._timeseries