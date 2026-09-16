def report(self, string='', level=0, prelude='', progress=False, abbreviate
    =True):
    if self._mute == False:
        self._prefix = prelude + '{spacing}[{name}] '.format(name=self.
            nametag, spacing=' ' * level)
        self._prefix = '{0:>16}'.format(self._prefix)
        equalspaces = ' ' * len(self._prefix)
        toprint = string + ''
        if abbreviate:
            if shortcuts is not None:
                for k in shortcuts.keys():
                    toprint = toprint.replace(k, shortcuts[k])
        if progress:
            print('\r' + self._prefix + toprint.replace('\n', '\n' +
                equalspaces))
        else:
            print(self._prefix + toprint.replace('\n', '\n' + equalspaces))