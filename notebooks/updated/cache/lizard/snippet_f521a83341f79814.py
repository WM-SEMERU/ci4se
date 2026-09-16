def lex(self, text, start=0):
    max = len(text)
    eaten = start
    s = self.state
    r = self.regexes
    toks = self.toks
    while eaten < max:
        for match in r[s].finditer(text, eaten):
            name = match.lastgroup
            tok = toks[name]
            toktext = match.group(name)
            eaten += len(toktext)
            yield tok.name, toktext
            if tok.next:
                s = tok.next
                break
    self.state = s