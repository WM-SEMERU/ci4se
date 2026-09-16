def main():
    out = ''
    UP = 0
    if '-h' in sys.argv:
        print(main.__doc__)
        sys.exit()
    if '-f' in sys.argv:
        ind = sys.argv.index('-f')
        file = sys.argv[ind + 1]
        DI = numpy.loadtxt(file, dtype=numpy.float)
    else:
        DI = numpy.loadtxt(sys.stdin, dtype=numpy.float)
    Ds = DI.transpose()[0]
    Is = DI.transpose()[1]
    if len(DI) > 1:
        XY = pmag.dimap_V(Ds, Is)
        for xy in XY:
            print('%f %f' % (xy[0], xy[1]))
    else:
        XY = pmag.dimap(Ds, Is)
        print('%f %f' % (XY[0], XY[1]))