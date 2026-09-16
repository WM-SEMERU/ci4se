def write_file(self, filename, file_format='xyz'):
    mol = pb.Molecule(self._obmol)
    return mol.write(file_format, filename, overwrite=True)