def apply(self, compound, orientation='', compound_port=''):
    compounds = list()
    if self.orientations.get(orientation):
        for port in self.orientations[orientation]:
            new_compound = clone(compound)
            new_port = new_compound.labels[compound_port]
            new_compound, new_port['up'], port['up']
            compounds.append(new_compound)
    else:
        for point in self.points:
            new_compound = clone(compound)
            new_compound.translate(point)
            compounds.append(new_compound)
    return compounds