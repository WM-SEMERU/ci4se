def pickledump(theobject, fname):
    fhandle = open(fname, 'wb')
    pickle.dump(theobject, fhandle)