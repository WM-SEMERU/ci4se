def possible_forms(self):
    forms = []
    for morph in self.modele().morphos():
        for desinence in self.modele().desinences(morph):
            radicaux = self.radical(desinence.numRad())
            if isinstance(radicaux, Radical):
                forms.append(radicaux.gr() + desinence.gr())
            else:
                for rad in radicaux:
                    forms.append(rad.gr() + desinence.gr())
    return list(set(forms))