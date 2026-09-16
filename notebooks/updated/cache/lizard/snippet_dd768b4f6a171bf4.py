def max_cation_insertion(self):
    lowest_oxid = defaultdict(lambda : 2, {'Cu': 1})
    oxid_pot = sum([((spec.oxi_state - min(e for e in Element(spec.symbol).
        oxidation_states if e >= lowest_oxid[spec.symbol])) * self.comp[
        spec]) for spec in self.comp if is_redox_active_intercalation(
        Element(spec.symbol))])
    return oxid_pot / self.cation_charge