def convert(f, output=sys.stdout):
    r = f.read(11)
    if r == 'compressed\n':
        png(output, *decompress(f))
    else:
        png(output, *glue(f, r))