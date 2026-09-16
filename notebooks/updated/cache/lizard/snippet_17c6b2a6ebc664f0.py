def repeatingfieldsnames(fields):
    fnames = [field['field'][0] for field in fields]
    fnames = [bunchhelpers.onlylegalchar(fname) for fname in fnames]
    fnames = [fname for fname in fnames if bunchhelpers.intinlist(fname.
        split())]
    fnames = [(bunchhelpers.replaceint(fname), None) for fname in fnames]
    dct = dict(fnames)
    repnames = fnames[:len(list(dct.keys()))]
    return repnames