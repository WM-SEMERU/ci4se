def strings(self):
    livestates = set(state for state in self.states if self.islive(state))
    strings = []
    cstate = self.initial
    cstring = []
    if cstate in livestates:
        if cstate in self.finals:
            yield cstring
        strings.append((cstring, cstate))
    i = 0
    while i < len(strings):
        cstring, cstate = strings[i]
        if cstate in self.map:
            for symbol in sorted(self.map[cstate], key=key):
                nstate = self.map[cstate][symbol]
                nstring = cstring + [symbol]
                if nstate in livestates:
                    if nstate in self.finals:
                        yield nstring
                    strings.append((nstring, nstate))
        i += 1