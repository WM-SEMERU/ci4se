def _create_values_table(self):
    len_alph = len(self.alphabet)
    identificators_table = {k: {} for k in self.voc_values.keys()}
    identificators_sizes = {k: (-1) for k in self.voc_values.keys()}
    for lexem_type, vocabulary in self.voc_values.items():
        len_vocb = len(vocabulary)
        identificators_sizes[lexem_type] = ceil(log(len_vocb, len_alph))
        num2alph = lambda x, n: self.alphabet[x // len_alph ** n % len_alph]
        identificators = [[str(num2alph(x, n)) for n in range(
            identificators_sizes[lexem_type])] for x in range(len_alph **
            identificators_sizes[lexem_type])]
        zip_id_voc = zip_longest(identificators, vocabulary, fillvalue=None)
        for idt, voc in zip_id_voc:
            identificators_table[lexem_type][''.join(idt)] = voc
    return identificators_table, identificators_sizes