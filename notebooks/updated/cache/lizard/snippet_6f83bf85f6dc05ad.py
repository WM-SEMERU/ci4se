def add_site_states(self, site, states):
    for state in states:
        if state not in self.site_states[site]:
            self.site_states[site].append(state)