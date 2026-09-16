def get_cont_state(self, string, backward=False):
    if string is None:
        return ()
    for _ in self.parser(self.scanner(string, True), True):
        if backward and len(self.parser.state[0]):
            break
    state = tuple(self.parser.state)
    self.scanner.reset()
    self.parser.reset()
    return state