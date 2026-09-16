def replace_requirements(self, infilename, outfile_initial=None):
    infile = open(infilename, 'r')
    _indexes = tuple(z[0] for z in filter(lambda x: x[1] == infilename,
        enumerate(self.req_parents)))
    req_paths = tuple(z[1] for z in filter(lambda x: x[0] in _indexes,
        enumerate(self.req_paths)))
    req_linenos = tuple(z[1] for z in filter(lambda x: x[0] in _indexes,
        enumerate(self.req_linenos)))
    if outfile_initial:
        outfile = outfile_initial
    else:
        outfile = tempfile.TemporaryFile('w+')
    for i, line in enumerate(infile.readlines()):
        if i in req_linenos:
            req_path = req_paths[req_linenos.index(i)]
            if not req_path:
                continue
            req_file = self.replace_requirements(req_path)
            self.insert_requirement(outfile, req_file, req_path)
            req_file.close()
        else:
            outfile.write(line)
    infile.close()
    if not outfile_initial:
        outfile.seek(0)
    return outfile