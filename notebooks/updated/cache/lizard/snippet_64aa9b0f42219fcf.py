def posmap(args):
    p = OptionParser(posmap.__doc__)
    opts, args = p.parse_args(args)
    if len(args) != 3:
        sys.exit(p.print_help())
    frgscffile, fastafile, scf = args
    cmd = 'faOneRecord {0} {1}'.format(fastafile, scf)
    scffastafile = scf + '.fasta'
    if not op.exists(scffastafile):
        sh(cmd, outfile=scffastafile)
    sizesfile = scffastafile + '.sizes'
    sizes = Sizes(scffastafile).mapping
    scfsize = sizes[scf]
    logging.debug('`{0}` has length of {1}.'.format(scf, scfsize))
    gapsbedfile = scf + '.gaps.bed'
    if not op.exists(gapsbedfile):
        args = [scffastafile, '--bed', '--mingap=100']
        gaps(args)
    posmapfile = scf + '.posmap'
    if not op.exists(posmapfile):
        args = [frgscffile, scf]
        query(args)
    bedfile = scf + '.bed'
    if not op.exists(bedfile):
        args = [posmapfile]
        bed(args)
    bedpefile = scf + '.bedpe'
    pairsbedfile = scf + '.pairs.bed'
    if not (op.exists(bedpefile) and op.exists(pairsbedfile)):
        bed_to_bedpe(bedfile, bedpefile, pairsbedfile=pairsbedfile, ca=True)
    Coverage(bedfile, sizesfile)
    Coverage(pairsbedfile, sizesfile)