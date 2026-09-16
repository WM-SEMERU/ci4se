def get_cantera_composition_string(self, species_conversion=None):
    if self.composition_type in ['mole fraction', 'mass fraction']:
        factor = 1.0
    elif self.composition_type == 'mole percent':
        factor = 100.0
    else:
        raise ValueError('Unknown composition type: {}'.format(self.
            composition_type))
    if species_conversion is None:
        comps = ['{!s}:{:.4e}'.format(c.species_name, c.amount.magnitude /
            factor) for c in self.composition.values()]
    else:
        comps = []
        for c in self.composition.values():
            amount = c.amount.magnitude / factor
            idents = [getattr(c, s, False) for s in ['species_name',
                'InChI', 'SMILES']]
            present = [(i in species_conversion) for i in idents]
            if not any(present):
                comps.append('{!s}:{:.4e}'.format(c.species_name, amount))
            else:
                if len([i for i in present if i]) > 1:
                    raise ValueError(
                        'More than one conversion present for species {}'.
                        format(c.species_name))
                ident = idents[present.index(True)]
                species_replacement_name = species_conversion.pop(ident)
                comps.append('{!s}:{:.4e}'.format(species_replacement_name,
                    amount))
        if len(species_conversion) > 0:
            raise ValueError('Unknown species in conversion: {}'.format(
                species_conversion))
    return ', '.join(comps)