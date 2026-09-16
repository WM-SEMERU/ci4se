def ajModeles(self):
    sl = []
    lines = [line for line in lignesFichier(self.path('modeles.la'))]
    max = len(lines) - 1
    for i, l in enumerate(lines):
        if l.startswith('$'):
            varname, value = tuple(l.split('='))
            self.lemmatiseur._variables[varname] = value
            continue
        eclats = l.split(':')
        if (eclats[0] == 'modele' or i == max) and len(sl) > 0:
            m = self.parse_modele(sl)
            self.register_modele(m)
            sl = []
        sl.append(l)