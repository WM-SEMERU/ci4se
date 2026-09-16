def issue_instant_ok(self):
    upper = time_util.shift_time(time_util.time_in_a_while(days=1), self.
        timeslack).timetuple()
    lower = time_util.shift_time(time_util.time_a_while_ago(days=1), -self.
        timeslack).timetuple()
    issued_at = str_to_time(self.response.issue_instant)
    return lower < issued_at < upper