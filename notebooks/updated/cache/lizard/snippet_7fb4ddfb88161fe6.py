def parse(cls, spec, relative_to='', subproject_roots=None):
    spec_path, target_name = parse_spec(spec, relative_to=relative_to,
        subproject_roots=subproject_roots)
    return cls(spec_path, target_name)