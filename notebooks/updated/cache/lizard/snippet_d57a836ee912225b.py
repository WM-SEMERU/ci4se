def cleandata(inputlist):
    output = []
    for e in inputlist:
        new = []
        for f in e:
            if f == '--':
                new.append(None)
            else:
                new.append(float(f))
        output.append(new)
    return output