def complete(self, text, state):
    if self.use_main_ns:
        self.namespace = __main__.__dict__
    if state == 0:
        self.matches = self.attr_matches(text)
    try:
        return self.matches[state]
    except IndexError:
        return None