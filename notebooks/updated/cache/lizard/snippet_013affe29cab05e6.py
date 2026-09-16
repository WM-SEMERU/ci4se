def from_files(cls, filepaths, specie, step_skip=10, ncores=None,
    initial_disp=None, initial_structure=None, **kwargs):
    if ncores is not None and len(filepaths) > 1:
        import multiprocessing
        p = multiprocessing.Pool(ncores)
        vaspruns = p.imap(_get_vasprun, [(fp, step_skip) for fp in filepaths])
        analyzer = cls.from_vaspruns(vaspruns, specie=specie, initial_disp=
            initial_disp, initial_structure=initial_structure, **kwargs)
        p.close()
        p.join()
        return analyzer
    else:

        def vr(filepaths):
            offset = 0
            for p in filepaths:
                v = Vasprun(p, ionic_step_offset=offset, ionic_step_skip=
                    step_skip)
                yield v
                offset = -(v.nionic_steps - offset) % step_skip
        return cls.from_vaspruns(vr(filepaths), specie=specie, initial_disp
            =initial_disp, initial_structure=initial_structure, **kwargs)