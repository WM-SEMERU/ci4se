def clear_state(self):
    self.state = {}
    self.state['steps'] = []
    self.state['current_step'] = None
    self.state['scope'] = []
    self.state['counters'] = {}
    self.state['strings'] = {}
    for step in self.matchers:
        self.state[step] = {}
        self.state[step]['pending'] = {}
        self.state[step]['actions'] = []
        self.state[step]['counters'] = {}
        self.state[step]['strings'] = {}
        self.state[step]['recipe'] = False