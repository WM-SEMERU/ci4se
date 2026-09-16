def setup_regex(self):
    self._RX_INTERFACE = (
        '\\n\\s*interface\\s+(?P<name>[a-z0-9_]+)(\\s\\((?P<symbol>[.\\w+*=/-]+)\\))?(?P<contents>.+?)end\\s*interface\\s+(?P=name)?'
        )
    self.RE_INTERFACE = re.compile(self._RX_INTERFACE, re.I | re.DOTALL)