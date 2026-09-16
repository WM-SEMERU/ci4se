def parse(self, arguments):
    if not isinstance(arguments, list):
        arguments = [arguments]
    if self.present:
        values = self.value
    else:
        values = []
    for item in arguments:
        Flag.Parse(self, item)
        values.append(self.value)
    self.value = values