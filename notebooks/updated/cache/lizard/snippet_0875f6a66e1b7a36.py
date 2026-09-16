def histogram(inlist, numbins=10, defaultreallimits=None, printextras=0):
    if defaultreallimits != None:
        if type(defaultreallimits) not in [list, tuple] or len(
            defaultreallimits) == 1:
            lowerreallimit = defaultreallimits
            upperreallimit = 1.000001 * max(inlist)
        else:
            lowerreallimit = defaultreallimits[0]
            upperreallimit = defaultreallimits[1]
        binsize = (upperreallimit - lowerreallimit) / float(numbins)
    else:
        estbinwidth = (max(inlist) - min(inlist)) / float(numbins) + 1e-06
        binsize = (max(inlist) - min(inlist) + estbinwidth) / float(numbins)
        lowerreallimit = min(inlist) - binsize / 2
    bins = [0] * numbins
    extrapoints = 0
    for num in inlist:
        try:
            if num - lowerreallimit < 0:
                extrapoints = extrapoints + 1
            else:
                bintoincrement = int((num - lowerreallimit) / float(binsize))
                bins[bintoincrement] = bins[bintoincrement] + 1
        except:
            extrapoints = extrapoints + 1
    if extrapoints > 0 and printextras == 1:
        print('\nPoints outside given histogram range =', extrapoints)
    return bins, lowerreallimit, binsize, extrapoints