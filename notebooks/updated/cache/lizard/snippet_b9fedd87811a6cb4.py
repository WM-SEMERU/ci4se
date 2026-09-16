def push_state(self):
    new = dict(self.states[-1])
    self.states.append(new)
    return self.state