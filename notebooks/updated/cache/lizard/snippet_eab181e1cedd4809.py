def reverse_file(infile, outfile):
    with open(infile, 'rb') as inf:
        with open(outfile, 'wb') as outf:
            reverse_fd(inf, outf)