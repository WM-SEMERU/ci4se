def transform_entries(self, entries, terminal_compositions):
    new_entries = []
    if self.normalize_terminals:
        fractional_comp = [c.fractional_composition for c in
            terminal_compositions]
    else:
        fractional_comp = terminal_compositions
    sp_mapping = collections.OrderedDict()
    for i, comp in enumerate(fractional_comp):
        sp_mapping[comp] = DummySpecie('X' + chr(102 + i))
    for entry in entries:
        try:
            rxn = Reaction(fractional_comp, [entry.composition])
            rxn.normalize_to(entry.composition)
            if all([(rxn.get_coeff(comp) <= CompoundPhaseDiagram.amount_tol
                ) for comp in fractional_comp]):
                newcomp = {sp_mapping[comp]: (-rxn.get_coeff(comp)) for
                    comp in fractional_comp}
                newcomp = {k: v for k, v in newcomp.items() if v >
                    CompoundPhaseDiagram.amount_tol}
                transformed_entry = TransformedPDEntry(Composition(newcomp),
                    entry)
                new_entries.append(transformed_entry)
        except ReactionError:
            pass
    return new_entries, sp_mapping