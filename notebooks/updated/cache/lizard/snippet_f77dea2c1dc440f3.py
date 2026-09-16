def lz(inlist, score):
    z = (score - mean(inlist)) / samplestdev(inlist)
    return z