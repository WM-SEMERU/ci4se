def patch(nml_path, nml_patch, out_path=None):
    parser = Parser()
    return parser.read(nml_path, nml_patch, out_path)