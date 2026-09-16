def main():
    args = docopt(__doc__, version=__version__)
    if 'bam_coverage' in args:
        bam_coverage(args['<reference>'], args['<alignments>'], int(args[
            '<minmatch>']), min_mapq=int(args['--mapq']), min_len=float(
            args['--minlen']))