def setup_regex(self):
    self._RX_MODULE = (
        '(\\n|^)\\s*module\\s+(?P<name>[a-z0-9_]+)(?P<contents>.+?)end\\s*module'
        )
    self.RE_MODULE = re.compile(self._RX_MODULE, re.I | re.DOTALL)
    self._RX_PROGRAM = (
        '(\\n|^)\\s*program\\s+(?P<name>[a-z0-9_]+)(?P<contents>.+?)end\\s*program'
        )
    self.RE_PROGRAM = re.compile(self._RX_PROGRAM, re.I | re.DOTALL)
    self._RX_USE = (
        '^\\s*use\\s+(?P<name>[^,]+?)(\\s*,\\s+only\\s*:(?P<only>[A-Za-z0-9_\\s,]+?))?$'
        )
    self.RE_USE = re.compile(self._RX_USE, re.I | re.M)
    self._RX_PRIV = 'private.+?(type|contains)'
    self.RE_PRIV = re.compile(self._RX_PRIV, re.DOTALL | re.I)
    self._RX_PUBLIC = '\\n\\s*public\\s+(?P<methods>[A-Za-z0-9_,\\s&\\n]+)'
    self.RE_PUBLIC = re.compile(self._RX_PUBLIC, re.I)
    self._RX_MEMBERS = '(?P<preamble>.+?)(\\s+type[,\\s]|contains)'
    self.RE_MEMBERS = re.compile(self._RX_MEMBERS, re.DOTALL | re.I)
    self._RX_PRECOMP = '#endif'
    self.RE_PRECOMP = re.compile(self._RX_PRECOMP, re.I)