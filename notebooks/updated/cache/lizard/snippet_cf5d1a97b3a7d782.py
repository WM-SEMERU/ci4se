def dump2file(self, obj, filepath, override=False, **kwargs):
    if override is False:
        if os.path.isfile(filepath):
            raise _FileAlreadyExists(
                "The file {0} already exists. Use a different filepath, or set the 'override' kwarg to True."
                .format(filepath))
    if str(filepath[-3:]) not in self._save_funcs.keys():
        raise _FileTypeError(
            'The {0} file extension is not supported for dumping a MolecularSystem or a Molecule. Please use XYZ or PDB.'
            .format(str(filepath[-3:])))
    self._save_funcs[str(filepath[-3:])](obj, filepath, **kwargs)