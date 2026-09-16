def _read_frame(self):
    line = next(self._f)
    if line != 'ITEM: TIMESTEP\n':
        raise FileFormatError(
            "Expecting line 'ITEM: TIMESTEP' at the beginning of a time frame."
            )
    try:
        line = next(self._f)
        step = int(line)
    except ValueError:
        raise FileFormatError(
            "Could not read the step number. Expected an integer. Got '%s'" %
            line[:-1])
    line = next(self._f)
    if line != 'ITEM: NUMBER OF ATOMS\n':
        raise FileFormatError("Expecting line 'ITEM: NUMBER OF ATOMS'.")
    try:
        line = next(self._f)
        num_atoms = int(line)
    except ValueError:
        raise FileFormatError(
            "Could not read the number of atoms. Expected an integer. Got '%s'"
             % line[:-1])
    if num_atoms != self.num_atoms:
        raise FileFormatError('A variable number of atoms is not supported.')
    for i in range(4):
        next(self._f)
    line = next(self._f)
    if line != 'ITEM: ATOMS\n':
        raise FileFormatError("Expecting line 'ITEM: ATOMS'.")
    fields = [list() for i in range(len(self.units))]
    for i in range(self.num_atoms):
        line = next(self._f)
        words = line.split()[1:]
        for j in range(len(fields)):
            fields[j].append(float(words[j]))
    fields = [step] + [(np.array(field) * unit) for field, unit in zip(
        fields, self.units)]
    return fields