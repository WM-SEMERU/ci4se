def _state_removal_init(self):
    for state_i in self.mma.states:
        for state_j in self.mma.states:
            if state_i.stateid == state_j.stateid:
                self.l_transitions[state_i.stateid, state_j.stateid
                    ] = self.epsilon
            else:
                self.l_transitions[state_i.stateid, state_j.stateid
                    ] = self.empty
            for arc in state_i.arcs:
                if arc.nextstate == state_j.stateid:
                    if self.l_transitions[state_i.stateid, state_j.stateid
                        ] != self.empty:
                        self.l_transitions[state_i.stateid, state_j.stateid
                            ] += self.mma.isyms.find(arc.ilabel)
                    else:
                        self.l_transitions[state_i.stateid, state_j.stateid
                            ] = self.mma.isyms.find(arc.ilabel)