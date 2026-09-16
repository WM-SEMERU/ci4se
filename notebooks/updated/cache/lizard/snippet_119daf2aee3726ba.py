def allpaths(args):
    p = OptionParser(allpaths.__doc__)
    p.add_option('--ploidy', default='1', choices=('1', '2'), help=
        'Ploidy [default: %default]')
    opts, args = p.parse_args(args)
    if len(args) == 0:
        sys.exit(not p.print_help())
    folders = args
    for pf in folders:
        if not op.isdir(pf):
            continue
        assemble_dir(pf, target=['final.contigs.fasta',
            'final.assembly.fasta'], ploidy=opts.ploidy)