def fill_predictive_missing_parameters(self):
    if hasattr(self, 'host_name') and not hasattr(self, 'address'):
        self.address = self.host_name
    if hasattr(self, 'host_name') and not hasattr(self, 'alias'):
        self.alias = self.host_name
    if self.initial_state == 'd':
        self.state = 'DOWN'
    elif self.initial_state == 'x':
        self.state = 'UNREACHABLE'