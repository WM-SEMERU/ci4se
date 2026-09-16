def some(args):
    p = OptionParser(some.__doc__)
    p.add_option('--exclude', default=False, action='store_true', help=
        'Output sequences not in the list file [default: %default]')
    p.add_option('--uniprot', default=False, action='store_true', help=
        'Header is from uniprot [default: %default]')
    opts, args = p.parse_args(args)
    if len(args) != 3:
        sys.exit(p.print_help())
    fastafile, listfile, outfastafile = args
    outfastahandle = must_open(outfastafile, 'w')
    qualfile = get_qual(fastafile)
    names = set(x.strip() for x in open(listfile))
    if qualfile:
        outqualfile = outfastafile + '.qual'
        outqualhandle = open(outqualfile, 'w')
        parser = iter_fasta_qual(fastafile, qualfile)
    else:
        parser = SeqIO.parse(fastafile, 'fasta')
    num_records = 0
    for rec in parser:
        name = rec.id
        if opts.uniprot:
            name = name.split('|')[-1]
        if opts.exclude:
            if name in names:
                continue
        elif name not in names:
            continue
        SeqIO.write([rec], outfastahandle, 'fasta')
        if qualfile:
            SeqIO.write([rec], outqualhandle, 'qual')
        num_records += 1
    logging.debug('A total of %d records written to `%s`' % (num_records,
        outfastafile))