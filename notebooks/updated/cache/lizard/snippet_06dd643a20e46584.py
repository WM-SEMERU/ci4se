def past_active_subjunctive(self):
    subjunctive_root = self.sfg3et[:-1] if self.sng[-1] == 'a' else self.sfg3et
    forms = []
    if self.subclass in [1, 2]:
        forms.append(subjunctive_root + 'a')
        subjunctive_root = subjunctive_root[:-1] if subjunctive_root[-1
            ] == 'j' else subjunctive_root
        forms.append(subjunctive_root + 'ir')
        forms.append(subjunctive_root + 'i')
        forms.append(subjunctive_root + 'im')
        forms.append(subjunctive_root + 'ið')
        forms.append(subjunctive_root + 'i')
    elif self.subclass in [3, 4]:
        subjunctive_root = apply_i_umlaut(subjunctive_root)
        forms.append(subjunctive_root + 'a')
        subjunctive_root = subjunctive_root[:-1] if subjunctive_root[-1
            ] == 'j' else subjunctive_root
        forms.append(subjunctive_root + 'ir')
        forms.append(subjunctive_root + 'i')
        forms.append(subjunctive_root + 'im')
        forms.append(subjunctive_root + 'ið')
        forms.append(subjunctive_root + 'i')
    return forms