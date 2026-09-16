def from_string(string_data, file_format='xyz'):
    mols = pb.readstring(str(file_format), str(string_data))
    return BabelMolAdaptor(mols.OBMol)