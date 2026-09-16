def find_strings(self, string='.*'):
    for s, sa in self.strings.items():
        if re.match(string, s):
            yield sa