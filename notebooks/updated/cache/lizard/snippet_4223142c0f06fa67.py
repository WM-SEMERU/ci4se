def match(self, keysequence: QtmacsKeysequence):
    try:
        macroName = self
        for _ in keysequence.toQtKeylist():
            macroName = macroName[_]
    except KeyError:
        return None, False
    if isinstance(macroName, dict):
        return None, True
    else:
        return macroName, True