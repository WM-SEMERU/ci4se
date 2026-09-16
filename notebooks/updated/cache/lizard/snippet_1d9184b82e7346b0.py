def convert_gempak_table(infile, outfile):
    r
    for line in infile:
        if not line.startswith('!') and line.strip():
            r, g, b = map(int, line.split())
            outfile.write('({0:f}, {1:f}, {2:f})\n'.format(r / 255, g / 255,
                b / 255))