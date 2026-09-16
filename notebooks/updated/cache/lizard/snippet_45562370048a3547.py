def _MapVowels(cls, string, also_p=False):
    return cls._PSUB_RE.sub(cls.Repl, string)