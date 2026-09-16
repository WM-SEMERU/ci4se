def savecands(d, cands, domock=False):
    with open(getcandsfile(d, domock=domock), 'w') as pkl:
        pickle.dump(d, pkl)
        pickle.dump(cands, pkl)