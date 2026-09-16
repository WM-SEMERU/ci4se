def log_prefix(self, prefix, *messages):
    if self.verbose:
        self.display(messages, prefix, debug=True)