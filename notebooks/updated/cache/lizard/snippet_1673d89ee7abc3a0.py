def _tot_unhandled_hosts_by_state(self, state):
    return sum(1 for h in self.hosts if h.state == state and h.state_type ==
        'HARD' and h.is_problem and not h.problem_has_been_acknowledged)