def _parse_geometry(self, geom):
    atoms = []
    for i, line in enumerate(geom.splitlines()):
        sym, atno, x, y, z = line.split()
        atoms.append(Atom(sym, [float(x), float(y), float(z)], id=i))
    return Molecule(atoms)