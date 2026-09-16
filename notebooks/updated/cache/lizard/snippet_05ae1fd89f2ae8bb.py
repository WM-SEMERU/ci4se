def from_file(filename, file_format='xyz'):
    mols = list(pb.readfile(str(file_format), str(filename)))
    return BabelMolAdaptor(mols[0].OBMol)