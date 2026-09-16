def command(self, function=None, prefix=None, unobserved=False):
    captured_f = self.capture(function, prefix=prefix)
    captured_f.unobserved = unobserved
    self.commands[function.__name__] = captured_f
    return captured_f