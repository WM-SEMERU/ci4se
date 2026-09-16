def _match_transition(self, transition):
    return (self.names == '*' or transition in self.names or transition.
        name in self.names)