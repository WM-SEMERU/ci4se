def log(self, msg, error=False):
    output = self.stdout
    if error:
        output = self.stderr
    output.write(msg)
    output.write('\n')