def lex(self, text):
    for match in self.regex.finditer(text):
        name = match.lastgroup
        yield name, match.group(name)