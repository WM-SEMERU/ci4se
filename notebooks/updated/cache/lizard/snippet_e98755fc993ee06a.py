def PushState(self, **_):
    if self.verbose:
        logging.debug('Storing state %r', self.state)
    self.state_stack.append(self.state)