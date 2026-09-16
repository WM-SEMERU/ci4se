def _update_simulation_end_from_lsm(self):
    te = self.l2g.xd.lsm.datetime[-1]
    simulation_end = te.replace(tzinfo=utc).astimezone(tz=self.tz).replace(
        tzinfo=None)
    if self.simulation_end is None:
        self.simulation_end = simulation_end
    elif self.simulation_end > simulation_end:
        self.simulation_end = simulation_end
    self._update_card('END_TIME', self.simulation_end.strftime(
        '%Y %m %d %H %M'))