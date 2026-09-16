def removeDuplicates(inFileName, outFileName):
    f = open(inFileName)
    legend = f.readline()
    data = ''
    h = {}
    h[legend] = 0
    lines = f.readlines()
    for l in lines:
        if not h.has_key(l):
            h[l] = 0
            data += l
    f.flush()
    f.close()
    f = open(outFileName, 'w')
    f.write(legend + data)
    f.flush()
    f.close()