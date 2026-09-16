def global_matches(self, text):
    import keyword
    matches = []
    seen = {'__builtins__'}
    n = len(text)
    for word in keyword.kwlist:
        if word[:n] == text:
            seen.add(word)
            matches.append(word)
    for nspace in [self.namespace, builtins.__dict__]:
        for word, val in nspace.items():
            if word[:n] == text and word not in seen:
                seen.add(word)
                matches.append(self._callable_postfix(val, word))
    return matches