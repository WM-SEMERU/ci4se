def centre_of_atoms(atoms, mass_weighted=True):
    points = [x._vector for x in atoms]
    if mass_weighted:
        masses = [x.mass for x in atoms]
    else:
        masses = []
    return centre_of_mass(points=points, masses=masses)