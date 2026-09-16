def merge_pexes(cls, path, pex_info, interpreter, pexes,
    interpeter_constraints=None):
    with cls.merged_pex(path, pex_info, interpreter, pexes,
        interpeter_constraints) as builder:
        builder.freeze()