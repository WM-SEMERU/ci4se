def gapmask(simseqs, origseqs):
    import numpy as np
    simdict = dict(simseqs)
    origdict = dict(origseqs)
    for k in origdict:
        origseq = np.array(list(origdict[k]))
        gap_pos = np.where(origseq == '-')
        simseq = np.array(list(simdict[k]))
        simseq[gap_pos] = '-'
        simdict[k] = ''.join(simseq)
    return list(simdict.items())