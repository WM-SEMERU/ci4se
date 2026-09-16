def blast(args):
    task_choices = ('blastn', 'blastn-short', 'dc-megablast', 'megablast',
        'vecscreen')
    p = OptionParser(blast.__doc__)
    p.set_align(pctid=0, evalue=0.01)
    p.add_option('--wordsize', type='int', help='Word size [default: %default]'
        )
    p.add_option('--best', default=1, type='int', help=
        'Only look for best N hits [default: %default]')
    p.add_option('--task', default='megablast', choices=task_choices, help=
        'Task of the blastn [default: %default]')
    p.set_cpus()
    opts, args = p.parse_args(args)
    if len(args) != 2:
        sys.exit(not p.print_help())
    reffasta, queryfasta = args
    blastfile = get_outfile(reffasta, queryfasta)
    run_megablast(infile=queryfasta, outfile=blastfile, db=reffasta,
        wordsize=opts.wordsize, pctid=opts.pctid, evalue=opts.evalue,
        hitlen=None, best=opts.best, task=opts.task, cpus=opts.cpus)
    return blastfile