def main(self, function):
    captured = self.command(function)
    self.default_command = captured.__name__
    return captured