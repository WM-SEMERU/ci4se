def merge(args):
    p = OptionParser(merge.__doc__)
    opts, args = p.parse_args(args)
    if len(args) < 2:
        sys.exit(not p.print_help())
    binfiles = args[:-1]
    mergedbin = args[-1]
    if op.exists(mergedbin):
        logging.error('`{0}` file exists. Remove before proceed.'.format(
            mergedbin))
        return
    b = BinFile(binfiles[0])
    ar = b.mmarray
    fastasize, = ar.shape
    logging.debug('Initialize array of uint16 with size {0}'.format(fastasize))
    merged_ar = np.zeros(fastasize, dtype=np.uint16)
    for binfile in binfiles:
        b = BinFile(binfile)
        merged_ar += b.array
    logging.debug('Resetting the count max to 255.')
    merged_ar[merged_ar > 255] = 255
    logging.debug('Compact array back to uint8 with size {0}'.format(fastasize)
        )
    merged_ar = np.array(merged_ar, dtype=np.uint8)
    merged_ar.tofile(mergedbin)
    logging.debug('Merged array written to `{0}`'.format(mergedbin))