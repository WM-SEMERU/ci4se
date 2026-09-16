def generateLatticeLine(self, latname='newline', line=None):
    latticeline = []
    for e in line:
        if isinstance(e, list):
            latticeline.extend(e)
        else:
            latticeline.append(e)
    newblele = {latname.upper(): {'beamline': {'lattice': '(' + ' '.join(
        latticeline) + ')'}}}
    self.all_elements.update(newblele)
    self.kws_bl.append(latname.upper())
    return newblele