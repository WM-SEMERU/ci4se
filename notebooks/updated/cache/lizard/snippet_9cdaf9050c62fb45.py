def initialize_path(self, path_num=None):
    self.state = copy(self.initial_state)
    return self.state