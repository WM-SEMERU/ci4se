def fixminimized(self, alphabet):
    insymbols = fst.SymbolTable()
    outsymbols = fst.SymbolTable()
    num = 1
    for char in self.alphabet:
        self.isyms.__setitem__(char, num)
        self.osyms.__setitem__(char, num)
        insymbols.add_symbol(char, num)
        outsymbols.add_symbol(char, num)
        num = num + 1
    self.automaton.set_input_symbols(insymbols)
    self.automaton.set_output_symbols(outsymbols)
    endstate = self.add_state()
    for state in self.states:
        for char in alphabet:
            found = 0
            for arc in state.arcs:
                if self.isyms.find(arc.ilabel) == char:
                    found = 1
                    break
            if found == 0:
                self.add_arc(state.stateid, endstate, char)
    self[endstate].final = False
    for char in alphabet:
        self.add_arc(endstate, endstate, char)