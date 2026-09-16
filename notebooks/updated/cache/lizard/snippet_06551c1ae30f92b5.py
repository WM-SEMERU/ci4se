def summarycanvas(args):
    p = OptionParser(summarycanvas.__doc__)
    opts, args = p.parse_args(args)
    if len(args) < 1:
        sys.exit(not p.print_help())
    for vcffile in args:
        counter = get_gain_loss_summary(vcffile)
        pf = op.basename(vcffile).split('.')[0]
        print(pf + ' ' + ' '.join('{}:{}'.format(k, v) for k, v in sorted(
            counter.items())))