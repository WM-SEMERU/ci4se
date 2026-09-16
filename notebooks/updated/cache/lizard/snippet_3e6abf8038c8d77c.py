def gen(ctx, num, lo, hi, size, struct):
    frmt = ctx.parent.params['frmt']
    action = ctx.parent.params['action']
    cryst = ase.io.read(struct, format=frmt)
    fn_tmpl = action
    if frmt == 'vasp':
        fn_tmpl += '_%03d.POSCAR'
        kwargs = {'vasp5': True, 'direct': True}
    elif frmt == 'abinit':
        fn_tmpl += '_%03d.abinit'
        kwargs = {}
    if verbose:
        from elastic.elastic import get_lattice_type
        nr, brav, sg, sgn = get_lattice_type(cryst)
        echo('%s lattice (%s): %s' % (brav, sg, cryst.get_chemical_formula()))
        if action == 'cij':
            echo('Generating {:d} deformations of {:.1f}(%/degs.) per axis'
                .format(num, size))
        elif action == 'eos':
            echo('Generating {:d} deformations from {:.3f} to {:.3f} of V0'
                .format(num, lo, hi))
    if action == 'cij':
        systems = elastic.get_elementary_deformations(cryst, n=num, d=size)
    elif action == 'eos':
        systems = elastic.scan_volumes(cryst, n=num, lo=lo, hi=hi)
    systems.insert(0, cryst)
    if verbose:
        echo('Writing %d deformation files.' % len(systems))
    for n, s in enumerate(systems):
        ase.io.write(fn_tmpl % n, s, format=frmt, **kwargs)