def init(self, states, accepted):
    self.statediag = []
    for key in states:
        self.statediag.append(states[key])
    self.quickresponse = {}
    self.quickresponse_types = {}
    self.quickresponse_types[0] = []
    self.quickresponse_types[1] = []
    self.quickresponse_types[2] = []
    self.quickresponse_types[3] = []
    self.quickresponse_types[4] = []
    for state in self.statediag:
        if state.id not in self.quickresponse:
            self.quickresponse[state.id] = [state]
        else:
            self.quickresponse[state.id].append(state)
        self.quickresponse_types[state.type].append(state)
    return self._stage(accepted, 0)