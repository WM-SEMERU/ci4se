def stack_files(files, hemi, source, target):
    import csv
    import os
    import numpy as np
    fname = 'sdist_%s_%s_%s.csv' % (hemi, source, target)
    filename = os.path.join(os.getcwd(), fname)
    alldist = []
    for dfile in files:
        alldist.append(np.genfromtxt(dfile, delimiter=','))
    alldist = np.array(alldist)
    alldist.tofile(filename, ',')
    return filename