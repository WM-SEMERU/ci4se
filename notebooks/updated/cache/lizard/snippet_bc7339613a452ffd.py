def __set_premature_stop_codon_status(self, hgvs_string):
    if re.search('.+\\*(\\d+)?$', hgvs_string):
        self.is_premature_stop_codon = True
        self.is_non_silent = True
        if hgvs_string.endswith('*'):
            self.is_nonsense_mutation = True
        else:
            self.is_nonsense_mutation = False
    else:
        self.is_premature_stop_codon = False
        self.is_nonsense_mutation = False