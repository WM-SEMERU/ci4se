def main():
    import getopt
    try:
        opts, args = getopt.getopt(sys.argv[1:], 'hv', ['help', 'version'])
    except getopt.GetoptError as err:
        sys.stderr.write('Error: %s\n' % err)
        exit(2)
    for opt, _ in opts:
        if opt in ['-h', '--help']:
            show_usage()
            exit()
        elif opt in ['-v', '--version']:
            show_version()
            exit()
    if len(args) != 2:
        show_usage()
        exit(1)
    infile, outfile = args
    if infile == outfile:
        sys.stderr.write('Error: outfile must differ from infile\n')
        exit(3)
    reverse_file(infile, outfile)
    sys.stdout.write('Successfully written to %s\n' % outfile)