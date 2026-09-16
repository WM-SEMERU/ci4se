def strip_to_chains(self, chains, break_at_endmdl=True):
    if chains:
        chains = set(chains)
        self.lines = [l for l in self.lines if not (l.startswith('ATOM  ') or
            l.startswith('HETATM') or l.startswith('ANISOU') or l.
            startswith('TER')) or l[21] in chains]
        if break_at_endmdl:
            new_lines = []
            for l in self.lines:
                if l.startswith('ENDMDL'):
                    new_lines.append(l)
                    break
                new_lines.append(l)
            self.lines = new_lines
        self._update_structure_lines()
    else:
        raise Exception('The chains argument needs to be supplied.')