def main(args=None):
    vinfo = sys.version_info
    if not vinfo >= (2, 7):
        raise SystemError(
            'Python interpreter version >= 2.7 required, found %d.%d instead.'
             % (vinfo.major, vinfo.minor))
    if args is None:
        parser = get_argument_parser()
        args = parser.parse_args()
    gene2acc_file = args.gene2acc_file
    output_file = args.output_file
    log_file = args.log_file
    quiet = args.quiet
    verbose = args.verbose
    log_stream = sys.stdout
    if output_file == '-':
        log_stream = sys.stderr
    logger = misc.get_logger(log_stream=log_stream, log_file=log_file,
        quiet=quiet, verbose=verbose)
    entrez2gene = read_gene2acc(gene2acc_file, logger)
    write_entrez2gene(output_file, entrez2gene, logger)
    return 0