def generate_pyxb_binding(self, args):
    pyxbgen_args = []
    pyxbgen_args.append("--schema-root='{}'".format(self.schema_dir))
    pyxbgen_args.append("--binding-root='{}'".format(self.binding_dir))
    pyxbgen_args.append(
        "--schema-stripped-prefix='https://repository.dataone.org/software/cicore/branches/D1_SCHEMA_v1.1/'"
        )
    pyxbgen_args.extend(args)
    self.run_pyxbgen(pyxbgen_args)