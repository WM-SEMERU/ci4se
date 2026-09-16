def get_snapshot(self, hosts, macromodulations, timeperiods):
    if self.snapshot_command is None:
        return
    if not self.snapshot_enabled:
        return
    boolmap = [self.is_state(s) for s in self.snapshot_criteria]
    if True not in boolmap:
        return
    now = int(time.time())
    cls = self.__class__
    if self.last_snapshot > now - self.snapshot_interval * cls.interval_length:
        return
    timeperiod = timeperiods[self.snapshot_period]
    if timeperiod is not None and not timeperiod.is_time_valid(now):
        return
    cls = self.__class__
    macroresolver = MacroResolver()
    data = self.get_data_for_event_handler(hosts)
    cmd = macroresolver.resolve_command(self.snapshot_command, data,
        macromodulations, timeperiods)
    reac_tag = self.snapshot_command.reactionner_tag
    event_h = EventHandler({'command': cmd, 'timeout': cls.
        event_handler_timeout, 'ref': self.uuid, 'reactionner_tag':
        reac_tag, 'is_snapshot': True})
    self.raise_snapshot_log_entry(self.snapshot_command)
    self.last_snapshot = now
    self.actions.append(event_h)