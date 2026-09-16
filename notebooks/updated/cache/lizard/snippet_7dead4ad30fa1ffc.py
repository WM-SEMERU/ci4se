def _prompt(self, prompt=None):
    if prompt:
        self.write(prompt)
        self.output.flush()
    return to_str(self.input.readline())