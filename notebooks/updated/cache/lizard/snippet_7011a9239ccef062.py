def compile_file(self, filename, ns):
    if self.parser.verbose:
        self.parser.log(_format('Compiling file {0!A}', filename))
    if not os.path.exists(filename):
        rfilename = self.find_mof(os.path.basename(filename[:-4]).lower())
        if rfilename is None:
            raise IOError(_format('No such file: {0!A}', filename))
        filename = rfilename
    with open(filename, 'r') as f:
        mof = f.read()
    return self.compile_string(mof, ns, filename=filename)