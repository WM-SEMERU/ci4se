def _parse_irc(self):
    irc_geoms = sections(re.escape('***** NEXT POINT ON IRC FOUND *****'),
        re.escape('INTERNUCLEAR DISTANCES (ANGS.)'), self.text)
    energies = [entry.splitlines()[5] for entry in irc_geoms]
    energies = [float(entry.split()[3]) for entry in energies]
    distances = [entry.splitlines()[4] for entry in irc_geoms]
    distances = [float(entry.split()[5]) for entry in distances]
    irc_geoms = ['\n'.join(i.splitlines()[11:-1]) for i in irc_geoms]
    irc_geoms = [self._parse_geometry(i) for i in irc_geoms]
    return {'geometries': irc_geoms, 'energies': energies, 'distances':
        distances}