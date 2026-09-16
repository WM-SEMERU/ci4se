def register(self, token, regexp):
    self._tokens.append((token, re.compile(regexp)))