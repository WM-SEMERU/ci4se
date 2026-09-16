def read_aims_output(filename):
    lines = open(filename, 'r').readlines()
    l = 0
    N = 0
    while l < len(lines):
        line = lines[l]
        if '| Number of atoms' in line:
            N = int(line.split()[5])
        elif '| Unit cell:' in line:
            cell = []
            for i in range(3):
                l += 1
                vec = lmap(float, lines[l].split()[1:4])
                cell.append(vec)
        elif 'Atomic structure:' in line or 'Updated atomic structure:' in line:
            if 'Atomic structure:' in line:
                i_sym = 3
                i_pos_min = 4
                i_pos_max = 7
            elif 'Updated atomic structure:' in line:
                i_sym = 4
                i_pos_min = 1
                i_pos_max = 4
            l += 1
            symbols = []
            positions = []
            for n in range(N):
                l += 1
                fields = lines[l].split()
                sym = fields[i_sym]
                pos = lmap(float, fields[i_pos_min:i_pos_max])
                symbols.append(sym)
                positions.append(pos)
        elif 'Total atomic forces' in line:
            forces = []
            for i in range(N):
                l += 1
                force = lmap(float, lines[l].split()[-3:])
                forces.append(force)
        l += 1
    atoms = Atoms_with_forces(cell=cell, symbols=symbols, positions=positions)
    atoms.forces = forces
    return atoms