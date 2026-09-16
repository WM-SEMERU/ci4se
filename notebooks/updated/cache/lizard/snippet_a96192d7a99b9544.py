def open(rootdir, mode='a'):
    rootsfile = os.path.join(rootdir, ROOTDIRS)
    if os.path.exists(rootsfile):
        return bquery.ctable(rootdir=rootdir, mode=mode)
    else:
        return bquery.carray(rootdir=rootdir, mode=mode)