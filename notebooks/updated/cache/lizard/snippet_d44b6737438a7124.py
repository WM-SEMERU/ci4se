def check_for_flexible_downtime(self, timeperiods, hosts, services):
    status_updated = False
    for downtime_id in self.downtimes:
        downtime = self.downtimes[downtime_id]
        if downtime.fixed or downtime.is_in_effect:
            continue
        if (downtime.start_time <= self.last_chk and downtime.end_time >=
            self.last_chk and self.state_id != 0 and downtime.trigger_id in
            ['', '0']):
            self.broks.extend(downtime.enter(timeperiods, hosts, services))
            status_updated = True
    if status_updated is True:
        self.broks.append(self.get_update_status_brok())