def transition(self, index, event_time):
    for state, affected in self._get_state_pops(index):
        if not affected.empty:
            state.next_state(affected.index, event_time, self.
                population_view.subview([self.state_column]))