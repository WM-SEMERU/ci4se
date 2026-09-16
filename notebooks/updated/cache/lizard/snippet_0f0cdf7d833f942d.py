def trim(args):
    p = OptionParser(trim.__doc__)
    p.add_option('-f', dest='first', default=0, type='int', help=
        'First base to keep. Default is 1.')
    p.add_option('-l', dest='last', default=0, type='int', help=
        'Last base to keep. Default is entire read.')
    opts, args = p.parse_args(args)
    if len(args) != 1:
        sys.exit(not p.print_help())
    fastqfile, = args
    obfastqfile = op.basename(fastqfile)
    fq = obfastqfile.rsplit('.', 1)[0] + '.ntrimmed.fastq'
    if fastqfile.endswith('.gz'):
        fq = obfastqfile.rsplit('.', 2)[0] + '.ntrimmed.fastq.gz'
    cmd = 'fastx_trimmer -Q33 '
    if opts.first:
        cmd += '-f {0.first} '.format(opts)
    if opts.last:
        cmd += '-l {0.last} '.format(opts)
    sh(cmd, infile=fastqfile, outfile=fq)