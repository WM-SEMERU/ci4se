def main():
    import optparse
    parser = optparse.OptionParser()
    parser.add_option('-w', '--width', dest='width', type='int', default=
        None, help='Width of printed image in characters.  Default: %default')
    options, args = parser.parse_args(args=sys.argv[1:])
    for imgpath in args:
        for line in Image(imgpath, options.width):
            printy(line)